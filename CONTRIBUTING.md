# Contributing

This wiki is open to everyone, and contributions of any size are welcome: fixing a typo, correcting a fact, improving an example, updating a vendor profile, or adding a whole new page.

## The quick way: edit in your browser

1. Open the page on the [site](https://nachi065.github.io/AI-Security-Wiki/) and click **Suggest an edit to this page** in the footer.
2. GitHub opens the page's Markdown file and creates your own copy (fork) of the repository automatically.
3. Make your change, describe it briefly, and choose **Propose changes**, then **Create pull request**.

That is all. You do not need to install anything or rebuild the HTML; the maintainer regenerates the pages when merging.

## The full way: work locally

1. Fork this repository and create a branch.
2. Edit or add Markdown under `source/`. Do not edit the `.html` files by hand; they are generated.
3. Rebuild the pages and run the author check:

   ```sh
   pip install markdown
   python3 build.py
   python3 check_author.py
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

## What to expect

- Every pull request is reviewed by the maintainer before it is merged.
- Keep content vendor-neutral and free of confidential, personal or organization-specific information.
- Not sure whether an idea fits? [Open an issue](https://github.com/nachi065/AI-Security-Wiki/issues) first.

## Credit and licence

Every page names its author in the page header, and the footer of the published page shows it. Credit can be added but never taken away.

- **A page you add is yours.** Put your own name in its `author:` line.
- **A substantial addition to someone else's page** is credited by adding a `coauthors:` line under `author:`, for example `coauthors: Your Name`. Several names are separated by commas.
- **Nobody's existing credit can be removed or replaced.** This protects every author and co-author equally, community members as much as the original author. An automated check compares each pull request with the main branch and fails it if it:
  - changes the `author:` of an existing page,
  - removes any existing co-author,
  - deletes or renames a page that carries a credit, or
  - removes or alters an existing line in `AUTHORS`.
- The check runs from the main branch, so editing the checker or workflow in a pull request has no effect on it.
- The wiki was created by **Nachiket Sathaye**, the original author. The pages he wrote are protected by the same rule.
- Add your name to the Contributors list in `AUTHORS` in your first pull request.
- By contributing, you agree that your contribution is licensed under [CC BY 4.0](LICENSE), the same licence as the rest of the wiki.
