# backend/tests/api/test_drug_coverage.py

import pytest
from fastapi.testclient import TestClient
from unittest.mock import MagicMock
from backend.app.main import app, medicare_client
from backend.app.services.drug_coverage_processor import DrugCoverageProcessor
from backend.app.models.medicare_api_models import DrugInfo, DrugAlternative, DrugRestriction
from backend.app.models.coverage_details import CoverageDetails

client = TestClient(app)

@pytest.fixture(autouse=True)
def mock_dependencies():
    medicare_client.get_drugs = MagicMock()
    DrugCoverageProcessor.process_coverage = MagicMock()

def test_get_drug_coverage_success():
    mock_drug_info = DrugInfo(
        drugName="TestDrug",
        alternatives=[],
        restrictions=[
            DrugRestriction(type="QL", simplifiedText="Limit 30 per month", rawText="Limit 30 per month"),
        ]
    )
    mock_coverage_details = CoverageDetails(
        plan_id="test_plan",
        drug_name="TestDrug",
        is_covered=True,
        tier="Tier 1",
        cost_sharing="$10 Copay",
        restrictions=["Limit 30 per month"]
    )
    medicare_client.get_drugs.return_value = mock_drug_info
    DrugCoverageProcessor.process_coverage.return_value = mock_coverage_details

    response = client.get("/api/drugs/coverage?plan_id=test_plan&drug_name=TestDrug")

    assert response.status_code == 200
    assert response.json() == {
        "plan_id": "test_plan",
        "drug_name": "TestDrug",
        "is_covered": True,
        "tier": "Tier 1",
        "cost_sharing": "$10 Copay",
        "restrictions": ["Limit 30 per month"]
    }
    medicare_client.get_drugs.assert_called_once_with("test_plan", "TestDrug")
    DrugCoverageProcessor.process_coverage.assert_called_once_with(mock_drug_info, "test_plan")

def test_get_drug_coverage_drug_not_found():
    medicare_client.get_drugs.return_value = None

    response = client.get("/api/drugs/coverage?plan_id=test_plan&drug_name=NonExistentDrug")

    assert response.status_code == 404
    assert response.json() == {"detail": "Drug information not found for the given plan and drug to check coverage."
}

def test_get_drug_coverage_no_coverage_details_found():
    mock_drug_info = DrugInfo(
        drugName="TestDrug",
        alternatives=[],
        restrictions=[]
    )
    medicare_client.get_drugs.return_value = mock_drug_info
    DrugCoverageProcessor.process_coverage.return_value = None

    response = client.get("/api/drugs/coverage?plan_id=test_plan&drug_name=TestDrug")

    assert response.status_code == 404
    assert response.json() == {"detail": "Drug coverage details not found for the given drug."
}
