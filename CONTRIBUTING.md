# Contributing

## Prerequisites

- [Python 3.12+](https://www.python.org/downloads/)
- [uv](https://docs.astral.sh/uv/getting-started/installation/)
- [git](https://git-scm.com/)

## Setup

```bash
git clone https://github.com/SbirLobo/SE4X-Companion.git
cd SE4X-Companion
cp .env.example .env
uv sync
uv run prek install --hook-type pre-commit --hook-type commit-msg
```

This installs all dependencies (app + dev tools) in a local `.venv` and sets up git hooks.

## Run

```bash
uv run se4x
```

Then open http://localhost:5000

## Git hooks

Pre-commit hooks are managed by [prek](https://prek.j178.dev/).

To install them manually:

```bash
uv run prek install --hook-type pre-commit --hook-type commit-msg
```

To run all hooks manually (on all files, not just staged ones):

```bash
uv run prek run --all-files
```

## Commit messages

This project follows [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/).

```
feat: add new feature
fix: fix a bug
docs: update documentation
refactor: restructure code without behavior change
test: add or update tests
chore: maintenance tasks
```

## Tests

```bash
uv run pytest --cov --cov-fail-under=100
# with an html file
uv run pytest --cov --cov-report=html && uv run python -m webbrowser htmlcov/index.html
```

100% code coverage is required. Every function must have unit tests.

## Add a dependency

App dependency:

```bash
uv add <package>
```

Dev dependency (test tools, linters, etc.):

```bash
uv add --group dev <package>
```
