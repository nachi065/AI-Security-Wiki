---
title: "Community Rules"
description: "Community rules for the AI Security Wiki: how author and co-author credit works, which changes are blocked automatically, and how to contribute a page."
author: Nachiket Sathaye
nav_order: 12
---

# Community Rules

This wiki is open for anyone to improve. These rules keep it fair: **everyone is credited for what they write, and nobody can take credit away from someone else.** Most of them are enforced automatically on every pull request.

## How credit works

Every page names its author in the page header, and the footer of the published page shows it.

```
---
title: "Your Page Title"
author: Your Name
coauthors: Another Person, A Third Person
---
```

| Field | Meaning |
|---|---|
| `author` | The person who wrote the page. Set once, when the page is created. |
| `coauthors` | People who later made a substantial addition. Optional; names separated by commas. |

A page you add is credited to you. A page someone else wrote stays credited to them, and you can be added alongside as a co-author.

## The credit rule: add, never take away

Credit can be added to a page but never removed or replaced. The rule protects every contributor equally, whether they wrote one page or sixty.

An automated check compares each pull request with the published version of the wiki. The table shows what it does with the changes people might try.

| # | What the pull request does | Outcome | Why |
|---|---|---|---|
| 1 | Adds a new page with the contributor's own name as `author` | **Allowed** | You are credited for your own work. |
| 2 | Adds the contributor to `coauthors` on an existing page | **Allowed** | Credit is being added, and nobody loses theirs. |
| 3 | Replaces the `author` of someone else's page with another name | **Blocked** | The original writer's credit would be erased. |
| 4 | Makes the contributor `author` and moves the real author down to `coauthors` | **Blocked** | The author of a page does not change, even if the name is kept elsewhere. |
| 5 | Removes an existing co-author | **Blocked** | Someone's credit would be removed. |
| 6 | Deletes or renames a page that carries a credit | **Blocked** | Removing the page removes the credit with it. |
| 7 | Removes or alters a name in the `AUTHORS` file | **Blocked** | The contributor list is add-only. |
| 8 | Edits the checker or its workflow to switch the rule off | **No effect** | The check always runs the version on the main branch, not the one in the pull request. |

### Worked examples

Suppose Jane Doe wrote a page and Ali Khan later co-authored it:

```
author: Jane Doe
coauthors: Ali Khan
```

**Allowed.** Bob Lee adds a section and credits himself alongside them:

```
author: Jane Doe
coauthors: Ali Khan, Bob Lee
```

**Blocked.** Bob replaces Jane:

```
author: Bob Lee
coauthors: Ali Khan
```

The check reports: *author must stay Jane Doe (found Bob Lee); add yourself under 'coauthors:' instead.*

**Blocked.** Bob promotes himself and demotes Jane:

```
author: Bob Lee
coauthors: Jane Doe, Ali Khan
```

Same result: the author of an existing page does not change.

**Blocked.** Bob drops Ali:

```
author: Jane Doe
```

The check reports: *co-author Ali Khan was removed.*

A blocked pull request cannot be merged until the credit is restored.

## What the check cannot judge

The check verifies that names are not removed. It cannot verify that a name deserves to be there. The maintainer reviews every pull request for the following, and will ask for changes or decline it:

- **Claiming co-authorship for a minor edit.** Fixing a typo or a link is a welcome contribution, and it is recorded in the Contributors list in `AUTHORS`, not as co-authorship of the page.
- **Submitting someone else's work as your own.** Only contribute text you wrote or have the right to share, and cite sources.
- **Adding a person without their knowledge.** Do not list someone as author or co-author unless they took part.

## Content rules

- **Stay vendor-neutral.** Describe capabilities and evidence. Do not promote or disparage a product.
- **No confidential, personal or organization-specific information.** Write so the page could apply to any organization.
- **Synthetic test data only.** Test cases must never contain real credentials, personal data or customer records.
- **Edit the Markdown under `source/`**, not the generated `.html` files.

## When a rule is broken

1. The automated check fails and the pull request cannot be merged.
2. The maintainer explains what needs to change.
3. Once the credit or content is corrected, the pull request is reviewed again in the normal way.

Corrections that genuinely need a credit changed, such as fixing a misspelt name or removing a page at its author's request, are made by the maintainer.

## Suggesting changes to these rules

These rules are not fixed. Suggestions from contributors are welcome, whether to change a rule, add one, or make the repository work better for the community.

A rule changes when two conditions are met:

1. **It is justified.** The proposal explains the problem with the current rule, what should change, and how the change benefits contributors and readers.
2. **It is mutually agreed.** The proposer and the maintainer discuss it openly and both agree on the final wording before anything changes.

How to propose a change:

1. [Open an issue](https://github.com/nachi065/AI-Security-Wiki/issues) titled "Rule proposal: …" and set out the justification.
2. Discuss it in the issue. Other contributors are welcome to add their views.
3. Once agreed, the change is made to this page, and to the automated check if the rule is one it enforces.

Until a proposal is agreed, the current rules continue to apply. A pull request that changes this page or the check without an agreed proposal will not be merged.

## Licence

Everything in the wiki is published under [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/). Anyone may reuse it with credit to the authors. By contributing, you agree to publish your contribution under the same licence.

The step-by-step guide to making a change is in [CONTRIBUTING.md](https://github.com/nachi065/AI-Security-Wiki/blob/main/CONTRIBUTING.md).
