"""Reference privacy duties in code: consent records, data principal rights,
retention, children's data and log redaction.

Standard library only, Python 3.10 or later. Written against India's Digital
Personal Data Protection Act 2023 (DPDP), but the patterns carry over to other
privacy laws. Each class names the duty it supports:

  DataMap            one file that says which fields are personal, why they
                     are held and for how long         -> privacy_map.json
  ConsentLedger      consent per purpose and notice version, withdrawal, and
                     the evidence to prove both          s.5, s.6(4), s.6(10)
  RightsDesk         access summary, correction, erasure, grievance,
                     nomination                          s.11 to s.14, s.8(10)
  RetentionRunner    erase when consent is withdrawn or the purpose is served,
                     with advance notice                 s.8(7), s.8(8)
  ChildrenGate       verified parental consent; no tracking, behavioural
                     monitoring or targeted advertising  s.9(1), s.9(3)
  RedactingLogger    personal fields replaced by keyed pseudonyms before they
                     reach a log                         s.8(5) safeguards

Time limits that the DPDP Rules 2025 set (the advance notice before erasure,
the grievance response time) are parameters, not constants. Set them from the
text that applies to you; see the Builder Track page for what was checked.

This is a teaching reference, not a compliance product. Using it does not make
a system compliant with any law.
"""
from __future__ import annotations

import hashlib
import hmac
import json
import time
import uuid
from dataclasses import dataclass, field
from pathlib import Path

from guard import AuditLog

DAY = 86400.0


# --------------------------------------------------------------------------
# The data map
# --------------------------------------------------------------------------

class DataMap:
    """Which fields are personal, the purposes they serve, how long they are kept."""

    def __init__(self, data: dict):
        self.system = data.get("system", "")
        self.categories = {c["name"]: c for c in data["categories"]}
        self.processors = data.get("processors", [])
        self._field = {f: c for c in data["categories"] for f in c["fields"]}

    @classmethod
    def load(cls, path: str | Path) -> "DataMap":
        return cls(json.loads(Path(path).read_text(encoding="utf-8")))

    def category(self, name: str) -> dict:
        if name not in self._field:
            raise KeyError(f"field '{name}' is not in the data map; classify it before storing it")
        return self._field[name]

    def is_personal(self, name: str) -> bool:
        c = self._field.get(name)
        return c is not None and c["sensitivity"] != "not-personal"

    def purposes(self) -> set[str]:
        return {p for c in self.categories.values() for p in c["purposes"]}


# --------------------------------------------------------------------------
# Log redaction
# --------------------------------------------------------------------------

class Pseudonymiser:
    """Keyed pseudonyms. A plain hash of an email or phone number can be reversed
    by hashing likely values; an HMAC cannot without the key. Keep the key in a
    secrets manager, not next to the logs."""

    def __init__(self, key: bytes):
        if len(key) < 32:
            raise ValueError("use a key of at least 32 bytes")
        self._key = key

    def token(self, value: object) -> str:
        return "p_" + hmac.new(self._key, str(value).encode(), hashlib.sha256).hexdigest()[:24]


class RedactingLogger:
    """Writes events to the tamper-evident audit log with every personal field
    replaced by its pseudonym. A field missing from the data map is refused,
    because an unclassified field is the usual way personal data reaches a log."""

    def __init__(self, audit: AuditLog, datamap: DataMap, pseudo: Pseudonymiser):
        self.audit, self.map, self.pseudo = audit, datamap, pseudo

    def redact(self, fields: dict) -> dict:
        out = {}
        for k, v in fields.items():
            self.map.category(k)  # raises on an unclassified field
            out[k] = self.pseudo.token(v) if self.map.is_personal(k) else v
        return out

    def event(self, action: str, actor: str, **fields) -> None:
        self.audit.write(action=action, actor=self.pseudo.token(actor), fields=self.redact(fields))


# --------------------------------------------------------------------------
# Consent
# --------------------------------------------------------------------------

GENERIC_PURPOSES = {"", "general", "any", "all", "other", "misc", "business purposes"}


class ConsentError(ValueError):
    pass


@dataclass
class Consent:
    purpose: str
    notice_version: str
    given_at: float
    withdrawn_at: float | None = None


class ConsentLedger:
    """Consent is recorded per purpose against the version of the notice the
    person saw. A new notice version needs new consent. Withdrawal is one call,
    as easy as giving consent. Every change goes to the audit log, which is the
    evidence that notice was given and consent obtained."""

    def __init__(self, datamap: DataMap, audit: AuditLog):
        self.map, self.audit = datamap, audit
        self._consents: dict[tuple[str, str], Consent] = {}

    def grant(self, principal: str, purpose: str, notice_version: str, now: float | None = None) -> None:
        if purpose.strip().lower() in GENERIC_PURPOSES or purpose not in self.map.purposes():
            raise ConsentError(f"purpose '{purpose}' is not a specific purpose in the data map")
        if not notice_version:
            raise ConsentError("record the version of the notice shown")
        now = time.time() if now is None else now
        self._consents[(principal, purpose)] = Consent(purpose, notice_version, now)
        self.audit.write(action="consent.grant", principal=principal, purpose=purpose, notice=notice_version)

    def withdraw(self, principal: str, purpose: str, now: float | None = None) -> None:
        c = self._consents.get((principal, purpose))
        if c and c.withdrawn_at is None:
            c.withdrawn_at = time.time() if now is None else now
            self.audit.write(action="consent.withdraw", principal=principal, purpose=purpose)

    def allows(self, principal: str, purpose: str, notice_version: str) -> bool:
        c = self._consents.get((principal, purpose))
        return c is not None and c.withdrawn_at is None and c.notice_version == notice_version

    def active_purposes(self, principal: str) -> set[str]:
        return {p for (who, p), c in self._consents.items() if who == principal and c.withdrawn_at is None}


# --------------------------------------------------------------------------
# Stored personal data
# --------------------------------------------------------------------------

@dataclass
class Store:
    """A stand-in for your database: values per person and field, and the time
    each person last approached you or used a right (s.8(8))."""
    values: dict[str, dict[str, object]] = field(default_factory=dict)
    last_seen: dict[str, float] = field(default_factory=dict)
    legal_holds: dict[str, str] = field(default_factory=dict)   # principal -> law that requires keeping the data

    def put(self, datamap: DataMap, principal: str, name: str, value: object, now: float) -> None:
        datamap.category(name)
        self.values.setdefault(principal, {})[name] = value
        self.last_seen[principal] = now


# --------------------------------------------------------------------------
# Rights
# --------------------------------------------------------------------------

@dataclass
class Ticket:
    id: str
    principal: str
    kind: str
    opened_at: float
    due_at: float
    text: str = ""


class RightsDesk:
    """Access, correction, erasure, grievance and nomination, each logged.
    response_days is the time limit you have set for answering; take it from
    the rules that apply to you."""

    def __init__(self, store: Store, datamap: DataMap, consent: ConsentLedger, audit: AuditLog,
                 response_days: int):
        self.store, self.map, self.consent, self.audit = store, datamap, consent, audit
        self.response_days = response_days
        self.tickets: list[Ticket] = []
        self.nominees: dict[str, str] = {}

    def _seen(self, principal: str, now: float) -> None:
        self.store.last_seen[principal] = now

    def access(self, principal: str, now: float) -> dict:
        """A summary of the personal data held and the processing, and who it was shared with."""
        self._seen(principal, now)
        held = self.store.values.get(principal, {})
        cats = {self.map.category(f)["name"] for f in held}
        summary = {
            "data": {f: v for f, v in held.items() if self.map.is_personal(f)},
            "purposes": sorted({p for c in cats for p in self.map.categories[c]["purposes"]}),
            "consented_purposes": sorted(self.consent.active_purposes(principal)),
            "shared_with": [{"name": p["name"], "country": p["country"],
                             "categories": sorted(set(p["categories"]) & cats)}
                            for p in self.map.processors if set(p["categories"]) & cats],
        }
        self.audit.write(action="rights.access", principal=principal)
        return summary

    def correct(self, principal: str, name: str, value: object, now: float) -> None:
        if name not in self.store.values.get(principal, {}):
            raise KeyError(f"no '{name}' held for this person")
        self.store.values[principal][name] = value
        self._seen(principal, now)
        self.audit.write(action="rights.correct", principal=principal, field=name)

    def erase(self, principal: str, now: float, reason: str = "request") -> list[str]:
        """Erase everything held, unless a law requires it to be kept. Returns the
        fields erased. Erase the same data from copies, caches, indexes and agent
        memory too; this store stands in for all of them."""
        if principal in self.store.legal_holds:
            self.audit.write(action="rights.erase.refused", principal=principal,
                             hold=self.store.legal_holds[principal])
            return []
        erased = sorted(self.store.values.pop(principal, {}))
        self.store.last_seen.pop(principal, None)
        self.audit.write(action="rights.erase", principal=principal, fields=erased, reason=reason)
        return erased

    def grievance(self, principal: str, text: str, now: float) -> Ticket:
        t = Ticket(uuid.uuid4().hex, principal, "grievance", now, now + self.response_days * DAY, text)
        self.tickets.append(t)
        self._seen(principal, now)
        self.audit.write(action="rights.grievance", principal=principal, ticket=t.id, due=t.due_at)
        return t

    def overdue(self, now: float) -> list[Ticket]:
        return [t for t in self.tickets if now > t.due_at]

    def nominate(self, principal: str, nominee: str, now: float) -> None:
        self.nominees[principal] = nominee
        self._seen(principal, now)
        self.audit.write(action="rights.nominate", principal=principal)

    def may_act_for(self, nominee: str, principal: str) -> bool:
        """A nominee may use the person's rights only if nominated. Checking the
        death or incapacity that triggers the nomination is a manual step."""
        return self.nominees.get(principal) == nominee


# --------------------------------------------------------------------------
# Retention
# --------------------------------------------------------------------------

class RetentionRunner:
    """Run daily. A person's data falls due for erasure when every purpose it was
    held for has lost its consent, or when the person has not been in touch for
    longer than the retention period of every category held. The person is told
    notice_hours before erasure; if they come back in that window, nothing is
    erased."""

    def __init__(self, store: Store, datamap: DataMap, consent: ConsentLedger, desk: RightsDesk,
                 audit: AuditLog, notice_hours: float, notify):
        self.store, self.map, self.consent, self.desk, self.audit = store, datamap, consent, desk, audit
        self.notice_hours, self.notify = notice_hours, notify
        self.pending: dict[str, float] = {}   # principal -> time the notice was sent

    def _due(self, principal: str, now: float) -> str | None:
        held = self.store.values.get(principal, {})
        cats = {self.map.category(f)["name"] for f in held if self.map.is_personal(f)}
        if not cats:
            return None
        needed = {p for c in cats for p in self.map.categories[c]["purposes"]}
        if not (needed & self.consent.active_purposes(principal)):
            return "consent withdrawn or never given"
        idle = now - self.store.last_seen.get(principal, now)
        if idle > max(self.map.categories[c]["retention_days"] for c in cats) * DAY:
            return "purpose no longer served"
        return None

    def run(self, now: float) -> list[str]:
        erased = []
        for principal in list(self.store.values):
            reason = self._due(principal, now)
            sent = self.pending.get(principal)
            if reason is None or principal in self.store.legal_holds:
                self.pending.pop(principal, None)
            elif sent is None:
                self.pending[principal] = now
                self.notify(principal, reason, now + self.notice_hours * 3600)
                self.audit.write(action="retention.notice", principal=principal, reason=reason)
            elif self.store.last_seen.get(principal, 0) > sent:
                self.pending.pop(principal)   # the person came back: the purpose is still served
            elif now - sent >= self.notice_hours * 3600:
                self.desk.erase(principal, now, reason=reason)
                self.pending.pop(principal)
                erased.append(principal)
        return erased


# --------------------------------------------------------------------------
# Children
# --------------------------------------------------------------------------

BARRED_FOR_CHILDREN = {"tracking", "behavioural-monitoring", "targeted-advertising"}


class ChildrenGate:
    """Before processing a child's data: a verified parental consent record must
    exist. Tracking, behavioural monitoring and targeted advertising are refused
    for children whatever the consent. How the parent is verified is a separate
    process; this gate only checks that it happened."""

    def __init__(self, audit: AuditLog, adult_age: int = 18):
        self.audit, self.adult_age = audit, adult_age
        self._parental: dict[str, str] = {}   # child -> reference of the verification record

    def record_parental_consent(self, child: str, verification_ref: str) -> None:
        if not verification_ref:
            raise ConsentError("a parental consent needs a verification reference")
        self._parental[child] = verification_ref
        self.audit.write(action="children.parental_consent", principal=child, ref=verification_ref)

    def check(self, principal: str, age: int | None, use: str) -> bool:
        child = age is None or age < self.adult_age   # unknown age is treated as a child
        if not child:
            return True
        ok = use not in BARRED_FOR_CHILDREN and principal in self._parental
        self.audit.write(action="children.check", principal=principal, use=use, allowed=ok)
        return ok
