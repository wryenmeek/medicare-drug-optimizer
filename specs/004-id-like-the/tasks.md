# Tasks: Pharmacy Network Optimization

**Input**: Design documents from `/specs/004-id-like-the/`
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
- [ ] T002 [P] Contract test `GET /api/pharmacies/preferences` endpoint (backend/tests/api/test_pharmacy_preferences.py).
- [ ] T003 [P] Contract test `GET /api/pharmacies/recommendations` endpoint (backend/tests/api/test_pharmacy_recommendations.py).
- [ ] T004 [P] Integration test for setting pharmacy preferences (frontend/tests/integration/test_pharmacy_preferences.jsx).
- [ ] T005 [P] Integration test for displaying pharmacy recommendations (frontend/tests/integration/test_pharmacy_recommendations.jsx).

## Phase 3.3: Core Implementation (ONLY after tests are failing)
- [ ] T006 Extend `medicare_api_client.py` to fetch comprehensive pharmacy data from Medicare API (backend/app/services/medicare_api_client.py).
- [ ] T007 Implement `Pharmacy` data model (backend/app/models/pharmacy.py).
- [ ] T008 Implement `UserPharmacyPreferences` data model (backend/app/models/user_pharmacy_preferences.py).
- [ ] T009 Implement `PharmacyRecommendation` data model (backend/app/models/pharmacy_recommendation.py).
- [ ] T010 Implement logic to filter pharmacies based on user preferences and API-provided coordinates (backend/app/services/pharmacy_optimizer.py).
- [ ] T011 Implement `GET /api/pharmacies/preferences` endpoint in FastAPI (backend/app/api/pharmacies.py).
- [ ] T012 Implement `POST /api/pharmacies/preferences` endpoint in FastAPI (backend/app/api/pharmacies.py).
- [ ] T013 Implement `GET /api/pharmacies/recommendations` endpoint in FastAPI (backend/app/api/pharmacies.py).
- [ ] T014 Implement frontend components for setting pharmacy preferences (frontend/src/components/PharmacyPreferences.jsx).
- [ ] T015 Implement frontend components for displaying pharmacy recommendations (frontend/src/components/PharmacyRecommendations.jsx).
- [ ] T016 Update frontend API client service to call new pharmacy endpoints (frontend/src/services/api.js).

## Phase 3.4: Integration
- [ ] T017 Integrate `pharmacy_optimizer` with `medicare_api_client` and FastAPI endpoints.
- [ ] T018 Integrate frontend components with backend API.

## Phase 3.5: Polish
- [ ] T019 [P] Unit tests for `pharmacy_optimizer.py` (backend/tests/services/test_pharmacy_optimizer.py).
- [ ] T020 [P] Unit tests for frontend components.
- [ ] T021 Update documentation (API docs for `/pharmacies`).

## Dependencies
- Tasks T002-T005 (Tests) must be completed before T006-T016 (Core Implementation).
- T006 (Extend API Client) blocks T010 (Optimizer Logic).
- T007-T009 (Data Models) block T010 (Optimizer Logic).
- T010 (Optimizer Logic) blocks T011-T013 (API Endpoints).
- T016 (Frontend API Client Update) blocks T018 (Frontend Integration).

## Parallel Example
```
# Launch T002-T005 (Tests) together:
Task: "Contract test GET /api/pharmacies/preferences endpoint"
Task: "Contract test GET /api/pharmacies/recommendations endpoint"
Task: "Integration test for setting pharmacy preferences"
Task: "Integration test for displaying pharmacy recommendations"

# Launch T019-T020 (Unit Tests) together:
Task: "Unit tests for pharmacy_optimizer.py"
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
