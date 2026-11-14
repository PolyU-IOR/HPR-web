# Publishing HPR-web

Source repository: <https://github.com/PolyU-IOR/HPR-web>.
Production domain: <https://hpr.top>.

Source upload and production deployment are separate operations. Use an existing
Git clone with the upstream history. A downloaded ZIP with a newly initialized
empty Git repository must not be pushed as a replacement for `main`.

## Prepare a source pull request

Start from the latest upstream `main` and use a new review branch. Keep the
existing repository and production branches intact. Install the dependencies
from `requirements-docs.lock`, then run `python tools/build_site.py`.

Review only these source paths and the generated `site/` snapshot:

- `.gitignore`, `CNAME`, `README.md`, `PUBLISHING.md`
- `build.bat`, `build.sh`, `push.txt`, `requirements-docs.txt`, `requirements-docs.lock`
- `landing/`, `assets/`, `docs/` excluding every `_build/`, `benchmarks/`, `tools/`
- `site/`, explicitly included because this repository publishes a built snapshot

Do not include `.venv/`, `tmp/`, `output/`, `.gh-pages/`, `_build/`, `__pycache__/`,
environment files, credentials, downloaded source archives or review screenshots.
The original upstream version tracked `.gh-pages/` and documentation `_build/`
directories. Remove those paths from Git tracking in the review branch; adding
ignore rules alone does not remove already tracked files or historical commits.

Inspect `git status --short`, `git diff --cached --stat`, and the staged diff.
Ensure the domain is `hpr.top`, both solvers build without warnings, local links
resolve, and the actual staged files have been scanned for secrets and local paths.
Commit the reviewed changes, then perform a dry run before the real branch push:

Before committing, check the repository-local `user.name` and `user.email`.
Commit authorship is public. Use the exact GitHub no-reply address from your
account's email settings when you want to keep your personal email private.
Never put a password or token into the remote URL or a tracked file.

```powershell
git push --dry-run origin HEAD
git push -u origin HEAD
```

These commands upload the current review branch. They do not merge it into `main`.
Open a pull request against `main`, review its Files changed page, and merge it
only after the exact commit has passed review. Do not force-push `main`.

## Deploy the reviewed website

Before production deployment, confirm in GitHub **Settings > Pages** which
branch and directory are configured. The repository has a `gh-pages` branch;
the steps below apply only when Pages uses `gh-pages` and its root directory.
Do not change Pages or DNS settings as part of an ordinary content update.

Prepare a separate clone of the latest `gh-pages` branch. Replace only the
website files in that dedicated clone with the reviewed generated `site/`
contents. Preserve its `.git` directory. Stage and inspect the resulting diff,
including the `CNAME` value and `.nojekyll` file. Commit the deployment there.

In the dedicated deployment clone, first confirm the remote URL, current branch,
and ancestry. Then use a normal fast-forward push:

```powershell
git push --dry-run origin HEAD:gh-pages
git push origin HEAD:gh-pages
```

Stop if Git rejects the update or the remote branch has changed; fetch and
review the newer remote state. Do not add `--force` to bypass rejection.
After GitHub Pages reports a successful deployment, check the homepage, LP and
QP documentation, images, download links, and return-to-home links on `hpr.top`.

Before deploying, record the previous `gh-pages` commit. To roll back, restore
that site's file tree as a new commit on top of the current `gh-pages` branch
and push normally. Do not reset or rewrite the shared branch history.
