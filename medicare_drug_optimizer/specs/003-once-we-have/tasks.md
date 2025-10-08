# Tasks: Drug Coverage Details and Restrictions

**Input**: Design documents from `/specs/003-once-we-have/`
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
- [ ] T002 [P] Contract test `GET /api/drugs/coverage` endpoint (backend/tests/api/test_drug_coverage.py).
- [ ] T003 [P] Integration test displaying detailed drug coverage and restrictions (frontend/tests/integration/test_drug_coverage_display.jsx).

## Phase 3.3: Core Implementation (ONLY after tests are failing)
- [ ] T004 Extend `medicare_api_client.py` to fetch detailed drug coverage and restrictions from Medicare API (backend/app/services/medicare_api_client.py).
- [ ] T005 Implement logic to process structured coverage details and restrictions from Medicare API (backend/app/services/drug_coverage_processor.py).
- [ ] T006 Implement `GET /api/drugs/coverage` endpoint in FastAPI (backend/app/api/drugs.py).
- [ ] T007 Implement `CoverageDetails` data model (backend/app/models/coverage_details.py).
- [ ] T008 Implement `UtilizationRestriction` data model (backend/app/models/utilization_restriction.py).
- [ ] T009 Implement frontend components to display detailed coverage and restrictions (frontend/src/components/DrugCoverageDisplay.jsx).
- [ ] T010 Update frontend API client service to call `GET /api/drugs/coverage` (frontend/src/services/api.js).

## Phase 3.4: Integration
- [ ] T011 Integrate `drug_coverage_processor` with `medicare_api_client` and FastAPI endpoint.
- [ ] T012 Integrate frontend `DrugCoverageDisplay` with backend API.

## Phase 3.5: Polish
- [ ] T013 [P] Unit tests for `drug_coverage_processor.py` (backend/tests/services/test_drug_coverage_processor.py).
- [ ] T014 [P] Unit tests for frontend components displaying coverage.
- [ ] T015 Update documentation (API docs for `/drugs/coverage`).

## Dependencies
- Tasks T002-T003 (Tests) must be completed before T004-T010 (Core Implementation).
- T004 (Extend API Client) blocks T005 (Processor Logic).
- T005 (Processor Logic) blocks T006 (API Endpoint).
- T007-T008 (Data Models) block T005 (Processor Logic).
- T010 (Frontend API Client Update) blocks T012 (Frontend Integration).

## Parallel Example
```
# Launch T002-T003 (Tests) together:
Task: "Contract test GET /api/drugs/coverage endpoint"
Task: "Integration test displaying detailed drug coverage and restrictions"

# Launch T013-T014 (Unit Tests) together:
Task: "Unit tests for drug_coverage_processor.py"
Task: "Unit tests for frontend components displaying coverage"
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
