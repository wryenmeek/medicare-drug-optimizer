# Tasks: GitHub Pages Deployment Strategy

**Input**: Design documents from `/specs/009-we-will-host/`
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
- [ ] T002 [P] Integration test for successful deployment to GitHub Pages (e.g., check public URL accessibility).
- [ ] T003 [P] Integration test for correct hash-based routing on GitHub Pages.

## Phase 3.3: Core Implementation (ONLY after tests are failing)
- [ ] T004 Configure frontend build process for GitHub Pages deployment (e.g., base URL, asset paths).
- [ ] T005 Implement hash-based routing in the frontend SPA.
- [ ] T006 Create GitHub Actions workflow (`.github/workflows/deploy-frontend.yml`) for automated deployment.
- [ ] T007 Configure frontend API communication for the GitHub Pages environment (e.g., environment variables for backend API URL).

## Phase 3.4: Integration
- [ ] T008 Integrate GitHub Actions workflow with frontend build process.

## Phase 3.5: Polish
- [ ] T009 [P] Unit tests for deployment scripts/configurations.
- [ ] T010 Update documentation (deployment guide, API URL configuration).

## Dependencies
- Tasks T002-T003 (Tests) must be completed before T004-T007 (Core Implementation).
- T004 (Build Configuration) blocks T006 (GitHub Actions Workflow).
- T005 (Hash-based Routing) blocks T003 (Routing Integration Test).
- T007 (API Communication Config) blocks T008 (Integration).

## Parallel Example
```
# Launch T002-T003 (Tests) together:
Task: "Integration test for successful deployment to GitHub Pages"
Task: "Integration test for correct hash-based routing on GitHub Pages"

# Launch T009 (Unit Tests) together:
Task: "Unit tests for deployment scripts/configurations"
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
