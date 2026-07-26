# dependency-management Specification

## Purpose
Defines how this project declares, locks, and installs its Python dependencies and dev tooling using `uv`.

## Requirements

### Requirement: Dependencies declared via pyproject.toml
The project SHALL declare its Python version constraint and dependencies in `pyproject.toml`, managed by `uv`, instead of `Pipfile`.

#### Scenario: Python version constraint preserved
- **WHEN** a contributor inspects `pyproject.toml`
- **THEN** it SHALL declare `requires-python` matching the Python 3.11 constraint previously specified in `Pipfile`'s `[requires]` section

#### Scenario: No Pipfile present
- **WHEN** a contributor inspects the repository root after this change
- **THEN** `Pipfile` and `Pipfile.lock` SHALL NOT be present

### Requirement: Dev dependencies locked via uv
The project SHALL provide a `uv.lock` file that locks the dev dependency group (`pylint`, `autopep8`) so environments are reproducible.

#### Scenario: Lock file committed
- **WHEN** a contributor inspects the repository root after this change
- **THEN** `uv.lock` SHALL be present and committed to version control

#### Scenario: Dev tools installable
- **WHEN** a contributor runs `uv sync`
- **THEN** `pylint` and `autopep8` SHALL be installed into the project's managed virtual environment

### Requirement: Documented uv-based workflow
The project's `README.md` SHALL document environment setup and script execution using `uv` commands instead of `pipenv` commands.

#### Scenario: Setup instructions use uv
- **WHEN** a contributor reads `README.md` to set up the project
- **THEN** the documented setup command SHALL reference `uv` (e.g., `uv sync`) rather than `pipenv install`

#### Scenario: Run instructions use uv
- **WHEN** a contributor reads `README.md` to run the splitter script
- **THEN** the documented run command SHALL reference `uv run` rather than `pipenv run`
