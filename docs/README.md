# GitHub Pages Setup

This folder is a GitHub Pages-ready static site for the book.

## Publish from the docs folder

1. Push this repository to GitHub.
2. Open repository Settings.
3. Go to Pages.
4. Set Source to `Deploy from a branch`.
5. Select branch `main` (or your default branch) and folder `/docs`.
6. Save.

After deployment, your site URL will be:

`https://<your-username>.github.io/<repo-name>/`

## Publish with GitHub Actions (recommended)

This repository includes a workflow at `.github/workflows/pages.yml` that deploys this folder automatically on every push to `main`.

1. Push your changes.
2. Open repository Settings.
3. Go to Pages.
4. Set Source to `GitHub Actions`.
5. Confirm the deploy succeeds in the Actions tab.

## Structure

- `index.html` home page
- `reader.html` markdown reader page
- `assets/` styles and scripts
- `catalog.json` content index
- `content/` copied markdown from chapters, appendices, and book front matter
- `.nojekyll` disables Jekyll processing for static file serving

## Notebook links

- Chapter cards and reader pages include an `Open Notebook` action when hosted on `github.io`.
- Notebook links are resolved to GitHub source paths automatically using the current owner/repo URL.

If your Pages host uses a custom domain or different repo/branch, edit [docs/assets/config.js](docs/assets/config.js):

```js
window.BOOK_CONFIG = {
	repoUrl: 'https://github.com/<owner>/<repo>',
	defaultBranch: 'main'
};
```

## Themes

The site supports three theme presets via [docs/assets/config.js](docs/assets/config.js):

- `clinical-journal` (default)
- `data-atlas`
- `lab-notebook`
- `material-docs`
- `sphinx-classic`

Example:

```js
window.BOOK_CONFIG = {
	repoUrl: 'https://github.com/<owner>/<repo>',
	defaultBranch: 'main',
	theme: 'data-atlas'
};
```

Users can also switch themes directly on hosted pages using the Theme dropdown in the home hero and reader header. The selected theme is saved in browser storage and reused on next visit.

## Updating content

When chapter markdown files are updated in the main repository, sync them to this site copy:

```bash
cp -R chapters docs/content/
find docs/content/chapters -type f ! -name '*.md' -delete
cp -R appendices docs/content/
find docs/content/appendices -type f ! -name '*.md' -delete
cp agentic_ai_cancer_research_book.md docs/content/
```
