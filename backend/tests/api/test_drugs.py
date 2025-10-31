import pytest
from fastapi.testclient import TestClient
from unittest.mock import MagicMock
from backend.app.models.medicare_api_models import DrugInfo, DrugAlternative, DrugRestriction
from backend.app.api.drugs import get_medicare_client

@pytest.fixture
def mock_medicare_client():
    return MagicMock()

@pytest.fixture
def client(mock_medicare_client):
    from backend.app.main import create_app
    app = create_app()
    app.dependency_overrides[get_medicare_client] = lambda: mock_medicare_client
    with TestClient(app) as c:
        yield c

def test_get_drugs_success(client, mock_medicare_client):
    mock_drug_info = DrugInfo(
        drugName="TestDrug",
        alternatives=[
            DrugAlternative(name="Alt1", category="Generic", estimatedAnnualCost=50.0),
            DrugAlternative(name="Alt2", category="Brand", estimatedAnnualCost=100.0),
        ],
        restrictions=[
            DrugRestriction(type="QL", simplifiedText="Limit 30 per month", rawText="Limit 30 per month"),
        ]
    )
    mock_medicare_client.get_drugs.return_value = mock_drug_info

    response = client.get("/api/drugs?plan_id=test_plan&drug_name=TestDrug")

    assert response.status_code == 200
    assert response.json() == {
        "drugName": "TestDrug",
        "alternatives": [
            {"name": "Alt1", "category": "Generic", "estimatedAnnualCost": 50.0},
            {"name": "Alt2", "category": "Brand", "estimatedAnnualCost": 100.0},
        ],
        "restrictions": [
            {"type": "QL", "simplifiedText": "Limit 30 per month", "rawText": "Limit 30 per month"},
        ]
    }
    mock_medicare_client.get_drugs.assert_called_once_with("test_plan", "TestDrug")

def test_get_drugs_not_found(client, mock_medicare_client):
    mock_medicare_client.get_drugs.return_value = None

    response = client.get("/api/drugs?plan_id=test_plan&drug_name=NonExistentDrug")

    assert response.status_code == 404
    assert response.json() == {"detail": "Drug information not found for the given plan and drug."}
