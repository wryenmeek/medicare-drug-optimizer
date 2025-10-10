# Tasks: Covered Drug Alternatives Discovery

**Input**: Design documents from `/specs/002-i-d-like/`

## Phase 3.1: Setup

- [X] T001 [P] Install `requests` library for making API calls to the RxClass API.

## Phase 3.2: Tests First (TDD) ⚠️ MUST COMPLETE BEFORE 3.3

**CRITICAL: These tests MUST be written and MUST FAIL before ANY implementation**

- [X] T002 [P] Contract test for `GET /api/drugs/{rxcui}/alternatives` in `backend/tests/api/test_drug_alternatives.py`.
- [X] T003 [P] Integration test for the drug alternatives feature in `frontend/tests/integration/test_drug_alternatives.spec.js`.

## Phase 3.3: Core Implementation (ONLY after tests are failing)

- [X] T004 [P] Implement `RxClass` data model in `backend/app/models/rxclass.py`.
- [X] T005 [P] Implement `Drug` and `DrugAlternative` data models in `backend/app/models/drug.py` and `backend/app/models/drug_alternative.py` respectively.
- [X] T006 Extend `medicare_service.py` in `backend/app/services/medicare_service.py` to fetch data from the RxClass API.
- [X] T007 Implement categorization logic for drug alternatives in a new service `backend/app/services/drug_alternatives_service.py`.
- [X] T008 Implement `GET /api/drugs/{rxcui}/alternatives` endpoint in `backend/app/api/drugs.py`.
- [X] T009 [P] Create a new frontend service in `frontend/src/services/drugAlternativesService.js` to call the new API endpoint.
- [X] T010 [P] Create a new React component in `frontend/src/components/DrugAlternatives.jsx` to display the drug alternatives.

## Phase 3.4: Integration

- [X] T011 Integrate the `DrugAlternatives` component into the drug details page.

## Phase 3.5: Polish

- [X] T012 [P] Add unit tests for the categorization logic in `backend/tests/services/test_drug_alternatives_service.py`.
- [X] T013 [P] Update the OpenAPI documentation to include the new endpoint.

## Dependencies

- T002 must be completed before T008.
- T003 must be completed before T011.
- T004 and T005 must be completed before T006 and T007.
- T006 and T007 must be completed before T008.
- T008 must be completed before T009.
- T009 and T010 must be completed before T011.

## Parallel Example

```
# Launch T002 and T003 together:
Task: "Contract test for GET /api/drugs/{rxcui}/alternatives in backend/tests/api/test_drug_alternatives.py"
Task: "Integration test for the drug alternatives feature in frontend/tests/integration/test_drug_alternatives.spec.js"

# Launch T004 and T005 together:
Task: "Implement RxClass data model in backend/app/models/rxclass.py"
Task: "Implement Drug and DrugAlternative data models in backend/app/models/drug.py and backend/app/models/drug_alternative.py respectively."
```
