import pytest
from fastapi.testclient import TestClient
from unittest.mock import MagicMock
from backend.app.models.medicare_api_models import DrugInfo, DrugAlternative, DrugRestriction
from backend.app.models.coverage_details import CoverageDetails
from backend.app.api.drugs import get_drug_coverage_processor, get_medicare_client

@pytest.fixture
def mock_medicare_client():
    return MagicMock()

@pytest.fixture
def mock_drug_coverage_processor():
    return MagicMock()

@pytest.fixture
def client(mock_medicare_client, mock_drug_coverage_processor):
    from backend.app.main import create_app
    app = create_app()
    app.dependency_overrides[get_medicare_client] = lambda: mock_medicare_client
    app.dependency_overrides[get_drug_coverage_processor] = lambda: mock_drug_coverage_processor
    with TestClient(app) as c:
        yield c

def test_get_drug_coverage_success(client, mock_medicare_client, mock_drug_coverage_processor):
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
    mock_medicare_client.get_drugs.return_value = mock_drug_info
    mock_drug_coverage_processor.process_coverage.return_value = mock_coverage_details

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
    mock_medicare_client.get_drugs.assert_called_once_with("test_plan", "TestDrug")
    mock_drug_coverage_processor.process_coverage.assert_called_once_with(mock_drug_info, "test_plan")

def test_get_drug_coverage_drug_not_found(client, mock_medicare_client):
    mock_medicare_client.get_drugs.return_value = None

    response = client.get("/api/drugs/coverage?plan_id=test_plan&drug_name=NonExistentDrug")

    assert response.status_code == 404
    assert response.json() == {"detail": "Drug information not found for the given plan and drug to check coverage."
}

def test_get_drug_coverage_no_coverage_details_found(client, mock_medicare_client, mock_drug_coverage_processor):
    mock_drug_info = DrugInfo(
        drugName="TestDrug",
        alternatives=[],
        restrictions=[]
    )
    mock_medicare_client.get_drugs.return_value = mock_drug_info
    mock_drug_coverage_processor.process_coverage.return_value = None

    response = client.get("/api/drugs/coverage?plan_id=test_plan&drug_name=TestDrug")

    assert response.status_code == 404
    assert response.json() == {"detail": "Drug coverage details not found for the given drug."
}
