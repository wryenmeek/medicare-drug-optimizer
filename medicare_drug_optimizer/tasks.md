# Consolidated Tasks: Medicare Drug Optimizer Project

This document outlines the consolidated, dependency-ordered tasks for the entire Medicare Drug Optimizer project, grouped by phases as per the approved roadmap.

## Phase 1: Project Setup & Core Integrations

### 1.1 Backend Setup (from Feature 001)
- [X] T001 Create backend project structure (`backend/app/api`, `backend/app/services`, `backend/tests`)
- [X] T002 Initialize Python project with FastAPI and Requests dependencies (`backend/requirements.txt`)
- [X] T003 [P] Configure backend linting (Ruff) and formatting (Black) (`backend/pyproject.toml`)

### 1.2 Frontend Setup (from Feature 008)
- [X] T004 Initialize React SPA project (`frontend/package.json`)
- [X] T005 Configure frontend build tools (e.g., Webpack/Vite, Babel) (`frontend/vite.config.js`)
- [X] T006 Install `ds-medicare-gov` and CMS Design System dependencies (`frontend/package.json`)
- [X] T007 [P] Configure frontend linting (ESLint) and formatting (Prettier) (`frontend/.eslintrc.js`, `frontend/.prettierrc.js`)
- [X] T008 [P] Set up Vitest for frontend unit and integration testing (`frontend/vite.config.js`)
- [X] T009 Implement basic SPA structure and routing (frontend/src/App.jsx, frontend/src/index.js)
- [X] T010 Integrate `ds-medicare-gov` components into the SPA.
- [X] T011 Implement fallback mechanism for missing `ds-medicare-gov` components using CMS Design System.
- [X] T012 Develop custom components adhering to Medicare Design System principles for remaining gaps.
- [X] T013 Implement frontend API client service (frontend/src/services/api.js).

### 1.3 Medicare API Client (from Feature 007)
- [X] T014 Implement `medicare_api_client.py` service structure (backend/app/services/medicare_api_client.py).
- [X] T015 Implement data models for `Plan`, `DrugInfo`, `DrugAlternative`, `DrugRestriction`, `Pharmacy` based on OpenAPI spec (backend/app/models/medicare_api_models.py).
- [X] T016 Implement data mapping from raw API responses to internal data models.
- [X] T017 Implement Referer header management for all API calls in `medicare_api_client.py`.
- [X] T018 Implement `get_plans` method in `medicare_api_client.py` to call `/plans` endpoint.
- [X] T019 Implement `get_drugs` method in `medicare_api_client.py` to call `/drugs` endpoint.
- [X] T020 Implement `get_pharmacies` method in `medicare_api_client.py` to call `/pharmacies` endpoint.
- [X] T021 Integrate `medicare_api_client` with FastAPI application.
- [X] T022 Implement robust error handling and logging for API calls.
- [X] T023 Configure CORS for frontend/backend communication.
- [X] T024 [P] Contract test `GET /plans` API endpoint (backend/tests/services/test_medicare_api_client.py).
- [X] T025 [P] Contract test `GET /drugs` API endpoint (backend/tests/services/test_medicare_api_client.py).
- [X] T026 [P] Contract test `GET /pharmacies` API endpoint (backend/tests/services/test_medicare_api_client.py).
- [X] T027 [P] Unit tests for `medicare_api_client.py` (backend/tests/services/test_medicare_api_client.py).
- [X] T028 [P] Unit tests for data mapping logic.

## Phase 2: Core Feature Development

### 2.1 Feature 001: Medicare Part D Drug Cost Optimizer
- [X] T029 Implement `PartDPlan` data model (backend/app/models/partd_plan.py).
- [X] T030 Implement `Drug` data model (backend/app/models/drug.py).
- [X] T031 Implement `Recommendation` data model (backend/app/models/recommendation.py).
- [X] T032 Implement `UserSession` data model (backend/app/models/user_session.py).
- [X] T033 Implement cost optimization logic (backend/app/services/optimizer.py).
- [X] T034 Implement `GET /api/plans` endpoint in FastAPI (backend/app/api/plans.py).
- [X] T035 Implement `GET /api/drugs` endpoint in FastAPI (backend/app/api/drugs.py).
- [X] T036 Implement `GET /api/pharmacies` endpoint in FastAPI (backend/app/api/pharmacies.py).
- [X] T037 Implement frontend components for plan selection (frontend/src/components/PlanSelector.jsx).
- [X] T038 Implement frontend components for drug list entry (frontend/src/components/DrugListEditor.jsx).
- [X] T039 Implement frontend components for displaying recommendations (frontend/src/components/RecommendationDisplay.jsx).
- [X] T040 [P] Integration test plan selection and drug list entry (frontend/tests/integration/test_plan_selection.jsx).
- [X] T041 [P] Integration test cost optimization recommendations display (frontend/tests/integration/test_recommendations.jsx).
- [X] T042 [P] Unit tests for `optimizer.py` (backend/tests/services/test_optimizer.py).
- [X] T043 [P] Unit tests for frontend components.

### 2.2 Feature 002: Covered Drug Alternatives Discovery
- [X] T044 Implement `DrugAlternative` data model (backend/app/models/drug_alternative.py).
- [X] T045 Implement logic to process Medicare API drug relationships and categorize alternatives (backend/app/services/drug_alternatives_processor.py).
- [X] T046 Implement `GET /api/drugs/alternatives` endpoint in FastAPI (backend/app/api/drugs.py).
- [X] T047 Implement frontend components to display categorized alternatives (frontend/src/components/DrugAlternativesDisplay.jsx).
- [X] T048 Update frontend API client service to call `GET /api/drugs/alternatives` (frontend/src/services/api.js).
- [X] T049 Integrate `drug_alternatives_processor` with `medicare_api_client` and FastAPI endpoint.
- [X] T050 Integrate frontend `DrugAlternativesDisplay` with backend API.
- [X] T051 [P] Contract test `GET /api/drugs/alternatives` endpoint (backend/tests/api/test_drug_alternatives.py).
- [X] T052 [P] Integration test displaying categorized drug alternatives (frontend/tests/integration/test_drug_alternatives_display.jsx).
- [X] T053 [P] Unit tests for `drug_alternatives_processor.py` (backend/tests/services/test_drug_alternatives_processor.py).
- [X] T054 [P] Unit tests for frontend components displaying alternatives.

### 2.3 Feature 003: Drug Coverage Details and Restrictions
- [X] T055 Implement `CoverageDetails` data model (backend/app/models/coverage_details.py).
- [X] T056 Implement `UtilizationRestriction` data model (backend/app/models/utilization_restriction.py).
- [X] T057 Implement logic to process structured coverage details and restrictions from Medicare API (backend/app/services/drug_coverage_processor.py).
- [X] T058 Implement `GET /api/drugs/coverage` endpoint in FastAPI (backend/app/api/drugs.py).
- [X] T059 Implement frontend components to display detailed coverage and restrictions (frontend/src/components/DrugCoverageDisplay.jsx).
- [X] T060 Update frontend API client service to call `GET /api/drugs/coverage` (frontend/src/services/api.js).
- [X] T061 Integrate `drug_coverage_processor` with `medicare_api_client` and FastAPI endpoint.
- [X] T062 Integrate frontend `DrugCoverageDisplay` with backend API.
- [X] T063 [P] Contract test `GET /api/drugs/coverage` endpoint (backend/tests/api/test_drug_coverage.py).
- [X] T064 [P] Integration test displaying detailed drug coverage and restrictions (frontend/tests/integration/test_drug_coverage_display.jsx).
- [X] T065 [P] Unit tests for `drug_coverage_processor.py` (backend/tests/services/test_drug_coverage_processor.py).
- [X] T066 [P] Unit tests for frontend components displaying coverage.

### 2.4 Feature 004: Pharmacy Network Optimization
- [X] T067 Implement `Pharmacy` data model (backend/app/models/pharmacy.py).
- [X] T068 Implement `UserPharmacyPreferences` data model (backend/app/models/user_pharmacy_preferences.py).
- [X] T069 Implement `PharmacyRecommendation` data model (backend/app/models/pharmacy_recommendation.py).
- [X] T070 Implement logic to filter pharmacies based on user preferences and API-provided coordinates (backend/app/services/pharmacy_optimizer.py).
- [X] T071 Implement `GET /api/pharmacies/preferences` endpoint in FastAPI (backend/app/api/pharmacies.py).
- [X] T072 Implement `POST /api/pharmacies/preferences` endpoint in FastAPI (backend/app/api/pharmacies.py).
- [X] T073 Implement `GET /api/pharmacies/recommendations` endpoint in FastAPI (backend/app/api/pharmacies.py).
- [X] T074 Implement frontend components for setting pharmacy preferences (frontend/src/components/PharmacyPreferences.jsx).
- [X] T075 Implement frontend components for displaying pharmacy recommendations (frontend/src/components/PharmacyRecommendations.jsx).
- [X] T076 Update frontend API client service to call new pharmacy endpoints (frontend/src/services/api.js).
- [X] T077 Integrate `pharmacy_optimizer` with `medicare_api_client` and FastAPI endpoint.
- [X] T078 Integrate frontend components with backend API.
- [X] T079 [P] Contract test `GET /api/pharmacies/preferences` endpoint (backend/tests/api/test_pharmacy_preferences.py).
- [X] T080 [P] Contract test `GET /api/pharmacies/recommendations` endpoint (backend/tests/api/test_pharmacy_recommendations.py).
- [X] T081 [P] Integration test for setting pharmacy preferences (frontend/tests/integration/test_pharmacy_preferences.jsx).
- [X] T082 [P] Integration test for displaying pharmacy recommendations (frontend/tests/integration/test_pharmacy_recommendations.jsx).
- [X] T083 [P] Unit tests for `pharmacy_optimizer.py` (backend/tests/services/test_pharmacy_optimizer.py).
- [X] T084 [P] Unit tests for frontend components.

### 2.5 Feature 005: Optimized Drug & Pharmacy Plan Generation
- [X] T085 Implement `FulfillmentPlan` data model (backend/app/models/fulfillment_plan.py).
- [X] T086 Implement `PlanComparison` data model (backend/app/models/plan_comparison.py).
- [X] T087 Implement multi-objective optimization algorithm (backend/app/services/optimization_service.py).
- [X] T088 Implement logic to generate "Lowest Cost" plan (backend/app/services/optimization_service.py).
- [X] T089 Implement logic to generate "Most Convenient" plan (backend/app/services/optimization_service.py).
- [X] T090 Implement logic to generate "Least Painful" plan (backend/app/services/optimization_service.py).
- [X] T091 Implement `GET /api/plans/optimized` endpoint in FastAPI (backend/app/api/plans.py).
- [X] T092 Implement frontend components to display optimized plans (frontend/src/components/OptimizedPlansDisplay.jsx).
- [X] T093 Implement frontend components to display plan comparisons (frontend/src/components/PlanComparisonDisplay.jsx).
- [X] T094 Update frontend API client service to call `GET /api/plans/optimized` (frontend/src/services/api.js).
- [X] T095 Integrate `optimization_service` with existing data services (medicare_api_client) and FastAPI endpoint.
- [X] T096 Integrate frontend components with backend API.
- [X] T097 [P] Contract test `GET /api/plans/optimized` endpoint (backend/tests/api/test_optimized_plans.py).
- [X] T098 [P] Integration test displaying optimized plans and comparisons (frontend/tests/integration/test_optimized_plans_display.jsx).
- [X] T099 [P] Unit tests for `optimization_service.py` (backend/tests/services/test_optimization_service.py).
- [X] T100 [P] Unit tests for frontend components.

## Phase 3: Deployment

### 3.1 Feature 009: GitHub Pages Deployment Strategy
- [X] T101 Configure frontend build process for GitHub Pages deployment (e.g., base URL, asset paths).
- [X] T102 Implement hash-based routing in the frontend SPA.
- [X] T103 Create GitHub Actions workflow (`.github/workflows/deploy-frontend.yml`) for automated deployment.
- [X] T104 Configure frontend API communication for the GitHub Pages environment (e.g., environment variables for backend API URL).
- [X] T105 Integrate GitHub Actions workflow with frontend build process.
- [X] T106 [P] Integration test for successful deployment to GitHub Pages (e.g., check public URL accessibility).
- [X] T107 [P] Integration test for correct hash-based routing on GitHub Pages.
- [X] T108 [P] Unit tests for deployment scripts/configurations.
