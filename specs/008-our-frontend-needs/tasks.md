# Tasks: Frontend Architecture & Medicare.gov Design System Integration

**Input**: Design documents from `/specs/008-our-frontend-needs/`
**Prerequisites**: plan.md (required), research.md, data-model.md, contracts/

## Format: `[ID] [P?] Description`
- **[P]**: Can run in parallel (different files, no dependencies)
- Include exact file paths in descriptions

## Path Conventions
- **Web app**: `backend/app/`, `frontend/src/`

## Phase 3.1: Setup
- [ ] T001 Initialize React SPA project (`frontend/package.json`)
- [ ] T002 Configure frontend build tools (e.g., Webpack/Vite, Babel) (`frontend/vite.config.js`)
- [ ] T003 Install `ds-medicare-gov` and CMS Design System dependencies (`frontend/package.json`)
- [ ] T004 [P] Configure frontend linting (ESLint) and formatting (Prettier) (`frontend/.eslintrc.js`, `frontend/.prettierrc.js`)
- [ ] T005 [P] Set up Vitest for frontend unit and integration testing (`frontend/vite.config.js`)

## Phase 3.2: Tests First (TDD) ⚠️ MUST COMPLETE BEFORE 3.3
**CRITICAL: These tests MUST be written and MUST FAIL before ANY implementation**
- [ ] T006 [P] Integration test for SPA routing (frontend/tests/integration/test_routing.jsx).
- [ ] T007 [P] Integration test for basic design system component rendering (frontend/tests/integration/test_design_system_components.jsx).

## Phase 3.3: Core Implementation (ONLY after tests are failing)
- [ ] T008 Implement basic SPA structure and routing (frontend/src/App.jsx, frontend/src/index.js).
- [ ] T009 Integrate `ds-medicare-gov` components into the SPA.
- [ ] T010 Implement fallback mechanism for missing `ds-medicare-gov` components using CMS Design System.
- [ ] T011 Develop custom components adhering to Medicare Design System principles for remaining gaps.
- [ ] T012 Implement frontend API client service (frontend/src/services/api.js).

## Phase 3.4: Integration
- [ ] T013 Integrate frontend with backend API (e.g., configure Axios/Fetch).

## Phase 3.5: Polish
- [ ] T014 [P] Unit tests for custom frontend components.
- [ ] T015 [P] Unit tests for design system integration.
- [ ] T016 Update frontend documentation (component usage, design guidelines).

## Dependencies
- Tasks T006-T007 (Tests) must be completed before T008-T012 (Core Implementation).
- T001-T005 (Setup) block T008 (SPA Structure).
- T009 (ds-medicare-gov Integration) blocks T010 (Fallback Mechanism).
- T010 (Fallback Mechanism) blocks T011 (Custom Components).
- T012 (Frontend API Client) blocks T013 (Frontend/Backend Integration).

## Parallel Example
```
# Launch T006-T007 (Tests) together:
Task: "Integration test for SPA routing"
Task: "Integration test for basic design system component rendering"

# Launch T014-T015 (Unit Tests) together:
Task: "Unit tests for custom frontend components"
Task: "Unit tests for design system integration"
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
