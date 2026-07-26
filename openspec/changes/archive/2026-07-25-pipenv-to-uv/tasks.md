## 1. Project Metadata

- [x] 1.1 Create `pyproject.toml` with project name, version, and `requires-python = ">=3.11,<3.12"`
- [x] 1.2 Add `[dependency-groups.dev]` (or `[tool.uv]` dev-dependencies) listing `pylint` and `autopep8`

## 2. Lock and Install

- [x] 2.1 Run `uv lock` to generate `uv.lock`
- [x] 2.2 Run `uv sync` and verify `pylint`/`autopep8` install into `.venv`
- [x] 2.3 Verify `uv run python3 splitter.py -h` runs successfully

## 3. Remove Pipenv Artifacts

- [x] 3.1 Delete `Pipfile`
- [x] 3.2 Delete `Pipfile.lock`
- [x] 3.3 Remove/update the pipenv-related comment block in `.gitignore`

## 4. Documentation

- [x] 4.1 Update `README.md` setup instructions to use `uv sync`
- [x] 4.2 Update `README.md` run instructions to use `uv run python3 splitter.py ...`
