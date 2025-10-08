# Tasks: Covered Drug Alternatives Discovery

**Input**: Design documents from `/specs/002-i-d-like/`
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
- [ ] T002 [P] Contract test `GET /api/drugs/alternatives` endpoint (backend/tests/api/test_drug_alternatives.py).
- [ ] T003 [P] Integration test displaying categorized drug alternatives (frontend/tests/integration/test_drug_alternatives_display.jsx).

## Phase 3.3: Core Implementation (ONLY after tests are failing)
- [ ] T004 Extend `medicare_api_client.py` to fetch drug alternative relationships from Medicare API (backend/app/services/medicare_api_client.py).
- [ ] T005 Implement logic to process Medicare API drug relationships and categorize alternatives (backend/app/services/drug_alternatives_processor.py).
- [ ] T006 Implement `GET /api/drugs/alternatives` endpoint in FastAPI (backend/app/api/drugs.py).
- [ ] T007 Implement `DrugAlternative` data model (backend/app/models/drug_alternative.py).
- [ ] T008 Implement frontend components to display categorized alternatives (frontend/src/components/DrugAlternativesDisplay.jsx).
- [ ] T009 Update frontend API client service to call `GET /api/drugs/alternatives` (frontend/src/services/api.js).

## Phase 3.4: Integration
- [ ] T010 Integrate `drug_alternatives_processor` with `medicare_api_client` and FastAPI endpoint.
- [ ] T011 Integrate frontend `DrugAlternativesDisplay` with backend API.

## Phase 3.5: Polish
- [ ] T012 [P] Unit tests for `drug_alternatives_processor.py` (backend/tests/services/test_drug_alternatives_processor.py).
- [ ] T013 [P] Unit tests for frontend components displaying alternatives.
- [ ] T014 Update documentation (API docs for `/drugs/alternatives`).

## Dependencies
- Tasks T002-T003 (Tests) must be completed before T004-T009 (Core Implementation).
- T004 (Extend API Client) blocks T005 (Processor Logic).
- T005 (Processor Logic) blocks T006 (API Endpoint).
- T007 (Data Model) blocks T005 (Processor Logic).
- T009 (Frontend API Client Update) blocks T011 (Frontend Integration).

## Parallel Example
```
# Launch T002-T003 (Tests) together:
Task: "Contract test GET /api/drugs/alternatives endpoint"
Task: "Integration test displaying categorized drug alternatives"

# Launch T012-T013 (Unit Tests) together:
Task: "Unit tests for drug_alternatives_processor.py"
Task: "Unit tests for frontend components displaying alternatives"
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
