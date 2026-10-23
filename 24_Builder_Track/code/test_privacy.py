"""Tests for privacy.py. Run:  python3 -m unittest -v test_privacy   (from this folder)"""
import json
import tempfile
import unittest
from pathlib import Path

from guard import AuditLog
from privacy import (DAY, ChildrenGate, ConsentError, ConsentLedger, DataMap, Pseudonymiser,
                     RedactingLogger, RetentionRunner, RightsDesk, Store)

HERE = Path(__file__).parent
KEY = b"unit-test-key-unit-test-key-0123456789"
T0 = 1_800_000_000.0


class Base(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.log_path = Path(self.tmp.name) / "audit.jsonl"
        self.audit = AuditLog(str(self.log_path))
        self.map = DataMap.load(HERE / "privacy_map.json")
        self.consent = ConsentLedger(self.map, self.audit)
        self.store = Store()
        self.desk = RightsDesk(self.store, self.map, self.consent, self.audit, response_days=30)
        self.notices = []
        self.runner = RetentionRunner(self.store, self.map, self.consent, self.desk, self.audit,
                                      notice_hours=48, notify=lambda *a: self.notices.append(a))

    def tearDown(self):
        self.tmp.cleanup()

    def add_person(self, who="u1"):
        self.consent.grant(who, "support-ticket", "v1", T0)
        self.store.put(self.map, who, "email", "asha@example.com", T0)
        self.store.put(self.map, who, "ticket_text", "my order is late", T0)

    def entries(self):
        return [json.loads(l) for l in self.log_path.read_text().splitlines()]


class DataMapTests(Base):
    def test_unclassified_field_is_refused(self):
        with self.assertRaises(KeyError):
            self.store.put(self.map, "u1", "passport_no", "X123", T0)

    def test_sensitivity(self):
        self.assertTrue(self.map.is_personal("email"))
        self.assertFalse(self.map.is_personal("request_id"))


class ConsentTests(Base):
    def test_generic_or_unknown_purpose_refused(self):
        for purpose in ("general", "marketing", ""):
            with self.assertRaises(ConsentError):
                self.consent.grant("u1", purpose, "v1", T0)

    def test_notice_version_change_needs_new_consent(self):
        self.consent.grant("u1", "support-ticket", "v1", T0)
        self.assertTrue(self.consent.allows("u1", "support-ticket", "v1"))
        self.assertFalse(self.consent.allows("u1", "support-ticket", "v2"))

    def test_withdrawal_stops_processing_and_is_evidenced(self):
        self.consent.grant("u1", "support-ticket", "v1", T0)
        self.consent.withdraw("u1", "support-ticket", T0 + 10)
        self.assertFalse(self.consent.allows("u1", "support-ticket", "v1"))
        actions = [e["action"] for e in self.entries()]
        self.assertEqual(actions, ["consent.grant", "consent.withdraw"])
        self.assertEqual(AuditLog.verify(str(self.log_path)), (True, 2))


class RightsTests(Base):
    def test_access_summary_names_purposes_and_recipients(self):
        self.add_person()
        s = self.desk.access("u1", T0 + 5)
        self.assertEqual(s["data"]["email"], "asha@example.com")
        self.assertIn("support-ticket", s["purposes"])
        self.assertEqual(s["shared_with"][0]["name"], "model-provider")
        self.assertEqual(s["shared_with"][0]["categories"], ["ticket-content"])

    def test_correction(self):
        self.add_person()
        self.desk.correct("u1", "email", "asha@example.org", T0 + 5)
        self.assertEqual(self.store.values["u1"]["email"], "asha@example.org")

    def test_erasure_and_legal_hold(self):
        self.add_person("u1")
        self.add_person("u2")
        self.store.legal_holds["u2"] = "tax record retention"
        self.assertEqual(self.desk.erase("u1", T0 + 5), ["email", "ticket_text"])
        self.assertNotIn("u1", self.store.values)
        self.assertEqual(self.desk.erase("u2", T0 + 5), [])
        self.assertIn("u2", self.store.values)

    def test_grievance_due_date_and_overdue(self):
        t = self.desk.grievance("u1", "no reply to my request", T0)
        self.assertEqual(t.due_at, T0 + 30 * DAY)
        self.assertEqual(self.desk.overdue(T0 + 29 * DAY), [])
        self.assertEqual(self.desk.overdue(T0 + 31 * DAY), [t])

    def test_nomination(self):
        self.desk.nominate("u1", "nominee-7", T0)
        self.assertTrue(self.desk.may_act_for("nominee-7", "u1"))
        self.assertFalse(self.desk.may_act_for("someone-else", "u1"))


class RetentionTests(Base):
    def test_withdrawal_leads_to_notice_then_erasure(self):
        self.add_person()
        self.consent.withdraw("u1", "support-ticket", T0 + DAY)
        self.assertEqual(self.runner.run(T0 + DAY), [])
        self.assertEqual(len(self.notices), 1)
        self.assertEqual(self.runner.run(T0 + DAY + 47 * 3600), [])
        self.assertEqual(self.runner.run(T0 + DAY + 48 * 3600), ["u1"])
        self.assertNotIn("u1", self.store.values)

    def test_inactivity_beyond_retention(self):
        self.add_person()
        self.assertEqual(self.runner.run(T0 + 100 * DAY), [])
        self.assertEqual(self.notices, [])
        # contact data is kept 365 days, ticket text 180: the longest period decides
        self.runner.run(T0 + 366 * DAY)
        self.assertEqual(len(self.notices), 1)
        self.assertEqual(self.runner.run(T0 + 368 * DAY), ["u1"])

    def test_coming_back_cancels_erasure(self):
        self.add_person()
        self.runner.run(T0 + 366 * DAY)
        self.desk.access("u1", T0 + 367 * DAY)          # the person logs in and uses a right
        self.assertEqual(self.runner.run(T0 + 368 * DAY), [])
        self.assertIn("u1", self.store.values)

    def test_legal_hold_blocks_retention_erasure(self):
        self.add_person()
        self.store.legal_holds["u1"] = "court order"
        self.consent.withdraw("u1", "support-ticket", T0 + DAY)
        self.runner.run(T0 + DAY)
        self.runner.run(T0 + 10 * DAY)
        self.assertIn("u1", self.store.values)


class ChildrenTests(Base):
    def test_child_needs_parental_consent(self):
        gate = ChildrenGate(self.audit)
        self.assertFalse(gate.check("c1", 15, "support-ticket"))
        gate.record_parental_consent("c1", "verification-ref-001")
        self.assertTrue(gate.check("c1", 15, "support-ticket"))

    def test_barred_uses_refused_even_with_consent(self):
        gate = ChildrenGate(self.audit)
        gate.record_parental_consent("c1", "verification-ref-001")
        for use in ("tracking", "behavioural-monitoring", "targeted-advertising"):
            self.assertFalse(gate.check("c1", 15, use))

    def test_adult_and_unknown_age(self):
        gate = ChildrenGate(self.audit)
        self.assertTrue(gate.check("a1", 30, "targeted-advertising"))
        self.assertFalse(gate.check("x1", None, "support-ticket"))


class RedactionTests(Base):
    def test_personal_fields_never_reach_the_log(self):
        log = RedactingLogger(self.audit, self.map, Pseudonymiser(KEY))
        log.event("ticket.update", "u1", email="asha@example.com", request_id="r-9")
        raw = self.log_path.read_text()
        self.assertNotIn("asha@example.com", raw)
        self.assertIn("r-9", raw)
        entry = self.entries()[-1]
        self.assertTrue(entry["fields"]["email"].startswith("p_"))

    def test_pseudonym_is_keyed_and_stable(self):
        a, b = Pseudonymiser(KEY), Pseudonymiser(KEY[::-1])
        self.assertEqual(a.token("x@example.com"), a.token("x@example.com"))
        self.assertNotEqual(a.token("x@example.com"), b.token("x@example.com"))
        with self.assertRaises(ValueError):
            Pseudonymiser(b"short")

    def test_unclassified_field_refused_in_logs(self):
        log = RedactingLogger(self.audit, self.map, Pseudonymiser(KEY))
        with self.assertRaises(KeyError):
            log.event("x", "u1", passport_no="X123")


if __name__ == "__main__":
    unittest.main()
