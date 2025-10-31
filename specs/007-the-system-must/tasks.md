# Tasks: Medicare.gov Plan Compare API Integration

**Input**: Design documents from `/specs/007-the-system-must/`
**Prerequisites**: plan.md (required), research.md, data-model.md, contracts/

## Format: `[ID] [P?] Description`
- **[P]**: Can run in parallel (different files, no dependencies)
- Include exact file paths in descriptions

## Path Conventions
- **Web app**: `backend/app/`, `frontend/src/`

## Phase 3.1: Setup
- [ ] T001 (No new setup tasks, relies on existing backend/frontend setup from Feature 001)

## Phase 3.2: Tests First (TDD) ⚠️ MUST COMPLETE BEFORE 3.3
**CRITICAL: These tests MUST be written and MUST FAIL before ANY implementation**
- [ ] T002 [P] Contract test `GET /plans` API endpoint (backend/tests/services/test_medicare_api_client.py).
- [ ] T003 [P] Contract test `GET /drugs` API endpoint (backend/tests/services/test_medicare_api_client.py).
- [ ] T004 [P] Contract test `GET /pharmacies` API endpoint (backend/tests/services/test_medicare_api_client.py).

## Phase 3.3: Core Implementation (ONLY after tests are failing)
- [ ] T005 Implement `medicare_api_client.py` service structure (backend/app/services/medicare_api_client.py).
- [ ] T006 Implement `get_plans` method in `medicare_api_client.py` to call `/plans` endpoint.
- [ ] T007 Implement `get_drugs` method in `medicare_api_client.py` to call `/drugs` endpoint.
- [ ] T008 Implement `get_pharmacies` method in `medicare_api_client.py` to call `/pharmacies` endpoint.
- [ ] T009 Implement Referer header management for all API calls in `medicare_api_client.py`.
- [ ] T010 Implement data models for `Plan`, `DrugInfo`, `DrugAlternative`, `DrugRestriction`, `Pharmacy` based on OpenAPI spec (backend/app/models/medicare_api_models.py).
- [ ] T011 Implement data mapping from raw API responses to internal data models.

## Phase 3.4: Integration
- [ ] T012 Integrate `medicare_api_client` with FastAPI application.
- [ ] T013 Implement robust error handling and logging for API calls.

## Phase 3.5: Polish
- [ ] T014 [P] Unit tests for `medicare_api_client.py` (backend/tests/services/test_medicare_api_client.py).
- [ ] T015 [P] Unit tests for data mapping logic.
- [ ] T016 Update documentation (API client usage, error codes).

## Dependencies
- Tasks T002-T004 (Tests) must be completed before T005-T011 (Core Implementation).
- T005 (Service Structure) blocks T006-T008 (API Methods).
- T009 (Referer Header) blocks T006-T008 (API Methods).
- T010 (Data Models) blocks T011 (Data Mapping).
- T011 (Data Mapping) blocks T006-T008 (API Methods).

## Parallel Example
```
# Launch T002-T004 (Contract Tests) together:
Task: "Contract test GET /plans API endpoint"
Task: "Contract test GET /drugs API endpoint"
Task: "Contract test GET /pharmacies API endpoint"

# Launch T014-T015 (Unit Tests) together:
Task: "Unit tests for medicare_api_client.py"
Task: "Unit tests for data mapping logic"
```

## Notes
- [P] tasks = different files, no dependencies
- Verify tests fail before implementing
- Commit after each task
- Avoid: vague tasks, same file conflicts

## Validation Checklist
- [ ] All contracts have corresponding tests
- [ ] All entities have model tasks
- [ ] All tests come before implementation
- [ ] Parallel tasks truly independent
- [ ] Each task specifies exact file path
- [ ] No task modifies same file as another [P] task
