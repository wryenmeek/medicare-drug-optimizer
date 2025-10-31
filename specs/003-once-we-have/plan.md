# Implementation Plan: Drug Coverage Details and Restrictions

**Branch**: `003-once-we-have` | **Date**: 2025-10-06 | **Spec**: [./spec.md](./spec.md)
**Input**: Feature specification from `specs/003-once-we-have/spec.md`

## Summary
This feature will display detailed coverage information for drugs and their alternatives, including how coverage varies by dosage, package size, and refill frequency. It will identify and simplify utilization management restrictions (Quantity Limits, Prior Authorization, Step Therapy) by leveraging the structured data provided directly by the Medicare API (Feature 007).

## Technical Context
**Language/Version**: Python 3.11, JavaScript (ES2022)
**Primary Dependencies**: FastAPI, Requests (for API calls to Medicare API), React, Zustand
**Storage**: N/A
**Testing**: Pytest, Vitest
**Target Platform**: Modern web browsers
**Project Type**: Web Application
**Constraints**: Relies on the Medicare API (Feature 007) providing drug restrictions in a structured/simplified format. If the API provides raw text, a minimal parsing component will still be necessary.

## Constitution Check
*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- **I. Simplicity and Clarity**: Leveraging structured data from the Medicare API simplifies the parsing logic significantly. The UI will present simplified information.
- **II. Test-Driven Development (TDD)**: TDD will be used for the logic that processes structured restriction data from the Medicare API and presents it to the user.
- **III. Automate Everything**: Automated tests will cover the processing of structured restriction data and the display of coverage details.
- **IV. Explicit Contracts**: The backend API will expose endpoints that provide structured coverage details and simplified restriction information, sourced directly from the Medicare API.
- **V. Secure by Design**: No new sensitive data is introduced. The processing logic will operate on data from the Medicare API.

## Project Structure

### Documentation (this feature)
```
specs/003-once-we-have/
├── plan.md              # This file
├── research.md          # Phase 0 output
├── data-model.md        # Phase 1 output
└── tasks.md             # Phase 2 output (/tasks command)
```

### Source Code (repository root)
This feature extends existing services.
```
backend/
├── app/
│   ├── api/
│   ├── services/        
│   │   ├── medicare_service.py  # Existing service, now handles structured restrictions
│   │   # formulary_parser_service.py removed or re-scoped if raw text is still present
│   └── main.py
└── tests/

frontend/
├── src/
│   ├── components/          # New components to display detailed coverage and restrictions
│   ├── pages/
│   └── services/       
└── tests/
```

**Structure Decision**: The existing frontend/backend monorepo structure is suitable. The `medicare_service` will be extended to handle structured restriction data from the Medicare API. A dedicated parsing service might be re-scoped or removed depending on the API's output format.

## Phase 0: Outline & Research
**Output**: `research.md` with all NEEDS CLARIFICATION resolved.

## Phase 1: Design & Contracts
**Output**: `data-model.md`

## Phase 2: Task Planning Approach
*This section describes what the /tasks command will do.*

**Task Generation Strategy**:
- Generate backend tasks for extending the `medicare_service` to fetch structured coverage details and restrictions from the Medicare API.
- Generate backend tasks for processing this structured data and presenting it to the frontend.
- Generate new API endpoints to serve the detailed coverage and restriction data.
- Generate frontend tasks to display this information in a user-friendly manner.

## Progress Tracking
- [X] Phase 0: Research complete
- [X] Phase 1: Design complete
- [ ] Phase 2: Task planning complete
- [ ] Phase 3: Tasks generated
- [ ] Phase 4: Implementation complete
- [ ] Phase 5: Validation passed

**Gate Status**:
- [X] Initial Constitution Check: PASS
- [ ] Post-Design Constitution Check: PENDING
- [X] All NEEDS CLARIFICATION resolved
- [ ] Complexity deviations documented
