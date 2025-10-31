# Tasks: Optimized Drug & Pharmacy Plan Generation

**Input**: Design documents from `/specs/005-once-the-app/`
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
- [ ] T002 [P] Contract test `GET /api/plans/optimized` endpoint (backend/tests/api/test_optimized_plans.py).
- [ ] T003 [P] Integration test displaying optimized plans and comparisons (frontend/tests/integration/test_optimized_plans_display.jsx).

## Phase 3.3: Core Implementation (ONLY after tests are failing)
- [ ] T004 Implement `FulfillmentPlan` data model (backend/app/models/fulfillment_plan.py).
- [ ] T005 Implement `PlanComparison` data model (backend/app/models/plan_comparison.py).
- [ ] T006 Implement multi-objective optimization algorithm (backend/app/services/optimization_service.py).
- [ ] T007 Implement logic to generate "Lowest Cost" plan (backend/app/services/optimization_service.py).
- [ ] T008 Implement logic to generate "Most Convenient" plan (backend/app/services/optimization_service.py).
- [ ] T009 Implement logic to generate "Least Painful" plan (backend/app/services/optimization_service.py).
- [ ] T010 Implement `GET /api/plans/optimized` endpoint in FastAPI (backend/app/api/plans.py).
- [ ] T011 Implement frontend components to display optimized plans (frontend/src/components/OptimizedPlansDisplay.jsx).
- [ ] T012 Implement frontend components to display plan comparisons (frontend/src/components/PlanComparisonDisplay.jsx).
- [ ] T013 Update frontend API client service to call `GET /api/plans/optimized` (frontend/src/services/api.js).

## Phase 3.4: Integration
- [ ] T014 Integrate `optimization_service` with existing data services (medicare_api_client) and FastAPI endpoint.
- [ ] T015 Integrate frontend components with backend API.

## Phase 3.5: Polish
- [ ] T016 [P] Unit tests for `optimization_service.py` (backend/tests/services/test_optimization_service.py).
- [ ] T017 [P] Unit tests for frontend components.
- [ ] T018 Update documentation (API docs for `/plans/optimized`).

## Dependencies
- Tasks T002-T003 (Tests) must be completed before T004-T013 (Core Implementation).
- T004-T005 (Data Models) block T006 (Optimization Algorithm).
- T006 (Optimization Algorithm) blocks T007-T009 (Plan Generation Logic).
- T007-T009 (Plan Generation Logic) block T010 (API Endpoint).
- T013 (Frontend API Client Update) blocks T015 (Frontend Integration).

## Parallel Example
```
# Launch T002-T003 (Tests) together:
Task: "Contract test GET /api/plans/optimized endpoint"
Task: "Integration test displaying optimized plans and comparisons"

# Launch T016-T017 (Unit Tests) together:
Task: "Unit tests for optimization_service.py"
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
