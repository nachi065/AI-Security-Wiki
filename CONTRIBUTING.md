# Contributing

This wiki is open to everyone, and contributions of any size are welcome: fixing a typo, correcting a fact, improving an example, or adding a whole new page.

## The quick way: edit in your browser

1. Open the page on the [site](https://nachi065.github.io/AI-Security-Wiki/) and click **Suggest an edit to this page** in the footer.
2. GitHub opens the page's Markdown file and creates your own copy (fork) of the repository automatically.
3. Make your change, describe it briefly, and choose **Propose changes**, then **Create pull request**.

That is all. You do not need to install anything or rebuild the HTML; the maintainer regenerates the pages when merging.

## The full way: work locally

1. Fork this repository and create a branch.
2. Edit or add Markdown under `source/`. Do not edit the `.html` files or the CSV files in `source/25_Templates/data/` by hand; they are generated.
3. Rebuild the pages and run the two checks:

   ```sh
   pip install markdown
   python3 build.py
   python3 check_author.py
   python3 check_links.py
   ```

4. Commit the Markdown and the regenerated HTML together, then open a pull request against `main`.

### Adding a new page

Create a `.md` file in the right section folder under `source/` and start it with:

```
---
title: "Your Page Title"
author: Your Name
parent: "Risk Management"
nav_order: 6
---
```

`author` is you: a page you add is credited to you, and your name appears in its footer. `parent` is the section title exactly as it appears in the sidebar, and `nav_order` sets the page's position in that section.

The footer also shows the date the page last changed, taken from the repository history. If you have checked a page against its sources, you can record that by adding `last_reviewed: 2026-10-10` (your own date, written as year-month-day) to the header. The line is optional.

## Regional sections: new regions are frozen

No new country or region section is added until the existing ones are verified. Status on 16 October 2026:

- **Checked against primary documents (in part):** EU (the omnibus regulation and its dates, 10 October 2026), India (six instruments, 16 October 2026), GCC (Saudi SDAIA documents, Bahrain PDPL title, UAE PDPL, 10 and 16 October 2026). Rows are tagged `[Verified]` only when the primary text was read; the source and retrieval date are recorded beside the row.
- **Not checked:** Australia, Brazil, Canada, China, Japan, Singapore, South Korea, UK and US. Treat every claim there as unverified until a page says otherwise.

A new region is accepted only when its first version has `[Verified]` rows for its main binding instruments, with a URL and retrieval date for each. Pull requests that add a region without that are asked to wait. Fixing or verifying an existing region is always welcome.

## What to expect

- Every pull request is reviewed and approved by the author (Nachiket Sathaye) or the co-author (Ankush Jain), and only they merge it. Your commits keep your name as their author after the merge.
- Do not type totals that the site can count (cases, layers, controls, risks, families). Write `{{n:tests}}`, `{{n:layer_tests}}`, `{{n:domain_tests}}`, `{{n:layers}}`, `{{n:controls}}`, `{{n:families}}`, `{{n:risks}}`, `{{n:critical}}`, `{{n:kit_cases}}` or a validation-level count such as `{{n:documented}}`; `build.py` fills them in and the link check fails on a hand-typed total. The list is in `counts.py`. Version-history rows and the Update Notes record what was true at the time and keep their numbers.
- Do not mark a test case as validated unless it has been run against a real system. A case shows its [validation level](https://nachi065.github.io/AI-Security-Wiki/10_Test_Case_Library/index.html#validation-levels) automatically; to record a run, add a `Validation Level` row (Lab-validated or Independently reproduced) and a `Validated Against` row with the product and version, the date (YYYY-MM-DD), the result and an evidence link. The link check rejects anything else.
- Never reuse or renumber an ID. Risk (AI-R), control (AI-CTRL) and test case (TC) numbers are permanent, because registers, workbooks and audits outside this wiki point at them. A new item takes the next unused number. To retire an item, keep its heading and ID, mark it **Retired** with the date and the reason, and name the item that replaces it, if any; do not delete it or give its number to something else.
- A new risk must pass the four tests in [What Belongs on the Register](https://nachi065.github.io/AI-Security-Wiki/02_Risk_Management/02A_AI_Risk_Methodology.html#what-belongs-on-the-register). A proposed risk that is turned down is recorded under Considered and Not Added on the register, with the reason.
- Give every new control a `Tier` field (Baseline or Advanced); the link check requires it.
- When you add a test case, leave out any field that the [Standard Fields](https://nachi065.github.io/AI-Security-Wiki/10_Test_Case_Library/standard-fields.html) page already covers (scoring, pass and fail criteria, reviewer notes, standard evidence, the lab setup for the layer). Write the field only when your case needs different wording. The link check fails if a case repeats a standard word for word. The standard wording itself is in `source/10_Test_Case_Library/standard-fields.json`.
- Two automated checks run on every pull request. One protects author credit. The other fails if a link inside the wiki points to a page or heading that does not exist, or if a page cites a risk, control or test case ID that is not defined. Links to other websites are checked weekly on the main branch, so a pull request never fails because an outside site moved a page.
- Keep content vendor-neutral and free of confidential, personal or organization-specific information.
- Not sure whether an idea fits? [Open an issue](https://github.com/nachi065/AI-Security-Wiki/issues) first.
- Think a rule should change? Suggestions are welcome. Rules change when a proposal is justified and mutually agreed with the maintainer; see [Suggesting changes to these rules](https://nachi065.github.io/AI-Security-Wiki/community-rules.html#suggesting-changes-to-these-rules).

## Credit and licence

Every page names its author in the page header, and the footer of the published page shows it. Credit can be added but never taken away. The [Community Rules](https://nachi065.github.io/AI-Security-Wiki/community-rules.html) page shows worked examples of what is allowed and what is blocked.

- **A page you add is yours.** Put your own name in its `author:` line.
- **A substantial addition to someone else's page** is credited by adding a `coauthors:` line under `author:`, for example `coauthors: Your Name`. Several names are separated by commas.
- **Nobody's existing credit can be removed or replaced.** This protects every author and co-author equally, community members as much as the original author. An automated check compares each pull request with the main branch and fails it if it:
  - changes the `author:` of an existing page,
  - removes any existing co-author,
  - deletes or renames a page that carries a credit, or
  - removes or alters an existing line in `AUTHORS`.
- The check runs from the main branch, so editing the checker or workflow in a pull request has no effect on it.
- The wiki was created by **Nachiket Sathaye**, the original author, and is co-authored by **Ankush Jain**. Their pages are protected by the same rule.
- Add your name to the Contributors list in `AUTHORS` in your first pull request.
- By contributing, you agree to license your contribution under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/), so that it can be published as part of the wiki under [CC BY-SA 4.0](LICENSE).
