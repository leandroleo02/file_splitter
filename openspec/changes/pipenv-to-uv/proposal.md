## Why

Pipenv is slow and largely unmaintained in comparison to modern alternatives. `uv` is a faster, actively maintained drop-in replacement for dependency management and virtual environments, and standardizing on it simplifies onboarding and CI.

## What Changes

- Replace `Pipfile` / `Pipfile.lock` with a `pyproject.toml` (uv-managed) and `uv.lock`.
- Move `pylint` and `autopep8` dev dependencies into the `[dependency-groups.dev]` section managed by uv.
- Preserve the `python_version = "3.11"` requirement via `requires-python` in `pyproject.toml`.
- Update `README.md` usage/setup instructions to reference `uv` commands instead of `pipenv`.
- Update `.gitignore` pipenv-specific comments/references as needed.
- **BREAKING**: Contributors must install and use `uv` instead of `pipenv` to manage the environment; `pipenv install` / `pipenv run` commands will no longer work.

## Capabilities

### New Capabilities
- `dependency-management`: How project dependencies and the dev environment are declared, locked, and installed (via `uv` instead of `pipenv`).

### Modified Capabilities
(none — no existing specs are affected)

## Impact

- Affected files: `Pipfile`, `Pipfile.lock` (removed), `pyproject.toml`, `uv.lock` (added), `README.md`, `.gitignore`.
- Affected systems: local developer setup and any CI that invokes `pipenv`.
- No changes to `splitter.py` or `splitter_dialect/` runtime behavior.
