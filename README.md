# Torii: GitHub-primary example

This small example shows a GitHub-primary Torii workflow. GitHub is the
source of truth. A private GitLab pull mirror is used for drafting and review;
after approval, a protected manual publish creates or updates the GitHub pull
request branch `gitlab-mr/<iid>`. GitHub owners merge that pull request. The
mirror then catches up and the original GitLab merge request closes.

This repository is an example, not an installed or security-certified gate.
It does not claim that a live pipeline or published pull request exists.

## Quickstart

```bash
git clone https://github.com/thompson-shaun/github-primary-example.git
cd github-primary-example
python3 hello.py Torii
python3 -m unittest discover -s tests -v
```

See [docs/usage.md](docs/usage.md) for the basic command examples.

The GitLab CI configuration is external to this mirror source on purpose, so
this repository intentionally has no `.gitlab-ci.yml`. Do not put tokens,
internal links, or internal artifacts in the repository.
