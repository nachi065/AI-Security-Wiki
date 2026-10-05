# Contributing

Contributions are welcome: corrections, new pages, and improvements to existing ones.

## How to contribute

1. Fork this repository and create a branch.
2. Edit the Markdown under `source/`. Do not edit the `.html` files by hand; they are generated.
3. Rebuild the pages and run the author check:

   ```sh
   pip install markdown
   python3 build.py
   python3 check_author.py
   ```

4. Commit the Markdown and the regenerated HTML together, then open a pull request against `main`.

Every pull request is reviewed by the repository owner before it is merged.

## Original author credit

The original author of this wiki is **Nachiket Sathaye**. That credit is fixed:

- Do not change or remove the "Original author" line in `AUTHORS`, the `ORIGINAL_AUTHOR` value in `build.py`, the author fields on the home page, or the footer on any page.
- `check_author.py` runs on every pull request and fails if any of these are altered.
- Add yourself to the Contributors list in `AUTHORS` instead.
