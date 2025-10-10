# Tasks: Medicare Part D Drug Cost Optimizer

**Input**: Design documents from `/specs/001-i-d-like/`
**Prerequisites**: plan.md (required), research.md, data-model.md, contracts/

## Format: `[ID] [P?] Description`
- **[P]**: Can run in parallel (different files, no dependencies)
- Include exact file paths in descriptions

## Path Conventions
- **Web app**: `backend/app/`, `frontend/src/`

## Phase 3.1: Setup
- [X] T001 Create backend project structure (`backend/app/api`, `backend/app/services`, `backend/tests`)
- [X] T002 Initialize Python project with FastAPI and Requests dependencies (`backend/requirements.txt`)
- [X] T003 [P] Configure backend linting (Ruff) and formatting (Black) (`backend/pyproject.toml`)
- [X] T004 Create frontend project structure (`frontend/src/components`, `frontend/src/pages`, `frontend/src/services`, `frontend/tests`)
- [X] T005 Initialize JavaScript project with React and Zustand dependencies (`frontend/package.json`)
- [X] T006 [P] Configure frontend linting (ESLint) and formatting (Prettier) (`frontend/.eslintrc.js`, `frontend/.prettierrc.js`)

## Phase 3.2: Tests First (TDD) ⚠️ MUST COMPLETE BEFORE 3.3
**CRITICAL: These tests MUST be written and MUST FAIL before ANY implementation**
- [X] T007 [P] Contract test `GET /api/plans` endpoint (backend/tests/api/test_plans.py)
- [X] T008 [P] Contract test `GET /api/drugs` endpoint (backend/tests/api/test_drugs.py)
- [X] T009 [P] Contract test `GET /api/pharmacies` endpoint (backend/tests/api/test_pharmacies.py)
- [X] T010 [P] Integration test for unauthenticated user workflow (frontend/tests/integration/test_unauthenticated_workflow.jsx)
- [X] T011 [P] Integration test for cost optimization recommendations display (frontend/tests/integration/test_recommendations_display.jsx)

## Phase 3.3: Core Implementation (ONLY after tests are failing)
- [X] T012 Implement `UserSession` data model (backend/app/models/user_session.py)
- [X] T013 Implement `PartDPlan` data model (backend/app/models/partd_plan.py)
- [X] T014 Implement `Drug` data model (backend/app/models/drug.py)
- [X] T015 Implement `Recommendation` data model (backend/app/models/recommendation.py)
- [X] T016 Implement `medicare_api_client.py` service for `medicare.gov` API interaction (backend/app/services/medicare_api_client.py)
- [X] T017 Implement `GET /api/plans` endpoint in FastAPI (backend/app/api/plans.py)
- [X] T018 Implement `GET /api/drugs` endpoint in FastAPI (backend/app/api/drugs.py)
- [X] T019 Implement `GET /api/pharmacies` endpoint in FastAPI (backend/app/api/pharmacies.py)
- [X] T020 Implement cost optimization logic (backend/app/services/optimizer.py)
- [X] T021 Implement frontend components for plan selection (frontend/src/components/PlanSelector.jsx)
- [X] T022 Implement frontend components for drug list entry (frontend/src/components/DrugListEditor.jsx)
- [X] T023 Implement frontend components for displaying recommendations (frontend/src/components/RecommendationDisplay.jsx)
- [X] T024 Implement frontend API client service (frontend/src/services/api.js)

## Phase 3.4: Integration
- [X] T025 Integrate `medicare_api_client` with FastAPI endpoints.
- [X] T026 Integrate frontend components with backend API.
- [X] T027 Implement error handling and logging for API calls.
- [X] T028 Configure CORS for frontend/backend communication.

## Phase 3.5: Polish
- [X] T029 [P] Unit tests for `medicare_api_client.py` (backend/tests/services/test_medicare_api_client.py).
- [X] T030 [P] Unit tests for `optimizer.py` (backend/tests/services/test_optimizer.py).
- [X] T031 [P] Unit tests for frontend components.
- [X] T032 Update documentation (README.md, API docs).

## Dependencies
- Tasks T007-T011 (Tests) must be completed before T012-T024 (Core Implementation).
- T012-T015 (Data Models) block T020 (Optimizer).
- T016 (API Client) blocks T017-T019 (API Endpoints).
- T020 (Optimizer) blocks T023 (Recommendation Display).
- T024 (Frontend API Client) blocks T026 (Frontend/Backend Integration).

## Parallel Example
```
# Launch T007-T009 (Backend API Contract Tests) together:
Task: "Contract test GET /api/plans endpoint"
Task: "Contract test GET /api/drugs endpoint"
Task: "Contract test GET /api/pharmacies endpoint"

# Launch T010-T011 (Frontend Integration Tests) together:
Task: "Integration test for unauthenticated user workflow"
Task: "Integration test for cost optimization recommendations display"

# Launch T029-T031 (Unit Tests) together:
Task: "Unit tests for medicare_api_client.py"
Task: "Unit tests for optimizer.py"
Task: "Unit tests for frontend components"
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