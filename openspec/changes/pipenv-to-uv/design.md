## Context

The project currently declares dependencies in a `Pipfile`/`Pipfile.lock` pair and is managed via `pipenv`. It has no runtime dependencies, only two dev dependencies (`pylint`, `autopep8`), and targets Python 3.11. This is a small, single-package script project, so the migration is low-risk but changes the contributor-facing workflow.

## Goals / Non-Goals

**Goals:**
- Replace `pipenv` with `uv` as the dependency manager and virtual environment tool.
- Preserve the existing Python version constraint (3.11) and dev dependency set.
- Keep contributor commands simple (`uv sync`, `uv run ...`).

**Non-Goals:**
- No change to `splitter.py` / `splitter_dialect/` runtime code or behavior.
- No packaging/publishing to PyPI (project remains a script, not a distributed package).
- No CI pipeline exists today, so none is added as part of this change.

## Decisions

- **Use `pyproject.toml` + `uv.lock` instead of `Pipfile`/`Pipfile.lock`.** This is uv's native format and the modern standard (PEP 621), replacing the Pipfile format entirely rather than trying to keep both.
- **Use `[dependency-groups.dev]` for `pylint`/`autopep8`.** This is uv's standard mechanism for dev-only dependencies, mirroring the `[dev-packages]` section in the old Pipfile.
- **Set `requires-python = ">=3.11,<3.12"`** (mirroring the exact pin in the old `Pipfile`'s `[requires]` section) to keep behavior equivalent rather than loosening the constraint.
- **Delete `Pipfile` and `Pipfile.lock`** rather than leaving them alongside the new files, to avoid confusion about which tool is authoritative.

## Risks / Trade-offs

- [Contributors with local `pipenv` muscle memory may run stale commands] → Update `README.md` with the new `uv` setup/run instructions.
- [Lock file resolution could differ slightly between pipenv and uv resolvers] → No pinned versions existed for dev deps (`*` in Pipfile), so there is no meaningful version drift risk here; `uv lock` will simply pick current latest-compatible versions.

## Migration Plan

1. Add `pyproject.toml` with project metadata, `requires-python`, and `[dependency-groups.dev]`.
2. Run `uv lock` to generate `uv.lock`.
3. Remove `Pipfile` and `Pipfile.lock`.
4. Update `README.md` and any pipenv-related `.gitignore` comments.
5. Verify `uv run python3 splitter.py --help` (or equivalent) works, and `uv run pylint`/`uv run autopep8` are usable.

No rollback beyond reverting the commit is needed since this only touches dependency tooling files.

## Open Questions

None.
