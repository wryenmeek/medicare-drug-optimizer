# Tasks: Use Poetry for Python Dependency Management

**Input**: Design documents from `/specs/010-use-poetry-to/`
**Prerequisites**: plan.md (required), research.md, data-model.md, contracts/

## Format: `[ID] [P?] Description`
- **[P]**: Can run in parallel (different files, no dependencies)
- Include exact file paths in descriptions

## Path Conventions
- **Single project**: `src/`, `tests/` at repository root
- **Web app**: `backend/src/`, `frontend/src/`

## Phase 3.1: Setup
- [X] T001 Install Poetry on the system (FR-006)
- [X] T002 Initialize Poetry project in the repository root (`poetry init`) (FR-005)
- [X] T003 Configure Poetry to manage the project's virtual environment (FR-002)
- [X] T004 Add existing Python dependencies from `backend/requirements.txt` to `pyproject.toml` using Poetry (FR-003, FR-008)
- [X] T005 Configure Poetry for Python 3.11 and 3.10 support (NFR-002)

## Phase 3.2: Tests First (TDD) ⚠️ MUST COMPLETE BEFORE 3.3
**CRITICAL: These tests MUST be written and MUST FAIL before ANY implementation**
- [X] T006 [P] Performance test for `poetry install` (NFR-001) (e.g., `tests/performance/test_poetry_install.py`)
- [X] T007 [P] Integration test for Poetry installation (FR-006) (e.g., `tests/integration/test_poetry_installation.py`)
- [X] T008 [P] Integration test for adding/updating dependencies (FR-003) (e.g., `tests/integration/test_dependency_management.py`)
- [X] T009 [P] Integration test for `requirements.txt` migration (FR-008) (e.g., `tests/integration/test_migration_utility.py`)

## Phase 3.3: Core Implementation (ONLY after tests are failing)
- [X] T010 Implement Poetry installation script/guide (FR-006) (e.g., `.specify/scripts/poetry_setup.ps1` or `docs/poetry_setup.md`)
- [X] T011 Implement `requirements.txt` migration utility/guide (FR-008) (e.g., `scripts/migrate_to_poetry.py` or `docs/migration_guide.md`)
- [X] T012 Update project setup documentation with Poetry usage (FR-005) (e.g., `README.md`)

## Phase 3.4: Integration
- [X] T013 Ensure existing backend tests (pytest) are compatible with Poetry's virtual environment.

## Phase 3.5: Polish
- [X] T014 [P] Unit tests for Poetry installation script/guide (e.g., `tests/unit/test_poetry_setup.py`)
- [X] T015 [P] Unit tests for `requirements.txt` migration utility (e.g., `tests/unit/test_migration_utility.py`)
- [X] T016 Update documentation with Poetry best practices and troubleshooting (e.g., `docs/poetry_best_practices.md`)

## Dependencies
- Setup tasks (T001-T005) must be completed before Test tasks (T006-T009).
- Test tasks (T006-T009) must be completed before Core Implementation tasks (T010-T012).
- Core Implementation tasks (T010-T012) must be completed before Integration tasks (T013).
- Integration tasks (T013) must be completed before Polish tasks (T014-T016).

## Parallel Example
```
# Launch T006-T009 (Tests) together:
Task: "Performance test for `poetry install`"
Task: "Integration test for Poetry installation"
Task: "Integration test for adding/updating dependencies"
Task: "Integration test for `requirements.txt` migration"

# Launch T013-T014 (Unit Tests) together:
Task: "Unit tests for Poetry installation script/guide"
Task: "Unit tests for `requirements.txt` migration utility"
```

## Notes
- [P] tasks = different files, no dependencies
- Verify tests fail before implementing
- Commit after each task
- Avoid: vague tasks, same file conflicts

## Validation Checklist
- [X] All contracts have corresponding tests
- [X] All entities have model tasks
- [X] All tests come before implementation
- [X] Parallel tasks truly independent
- [X] Each task specifies exact file path
- [X] No task modifies same file as another [P] task
