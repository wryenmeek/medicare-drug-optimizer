import pytest
from fastapi.testclient import TestClient
from unittest.mock import MagicMock
from backend.app.models.medicare_api_models import DrugInfo, DrugAlternative
from backend.app.api.drugs import get_drug_alternatives_processor, get_medicare_client

@pytest.fixture
def mock_medicare_client():
    return MagicMock()

@pytest.fixture
def mock_drug_alternatives_processor():
    return MagicMock()

@pytest.fixture
def client(mock_medicare_client, mock_drug_alternatives_processor):
    from backend.app.main import create_app
    app = create_app()
    app.dependency_overrides[get_medicare_client] = lambda: mock_medicare_client
    app.dependency_overrides[get_drug_alternatives_processor] = lambda: mock_drug_alternatives_processor
    with TestClient(app) as c:
        yield c

def test_get_drug_alternatives_success(client, mock_medicare_client, mock_drug_alternatives_processor):
    mock_drug_info = DrugInfo(
        drugName="TestDrug",
        alternatives=[
            DrugAlternative(name="Alt1", category="Generic", estimatedAnnualCost=50.0),
            DrugAlternative(name="Alt2", category="Brand", estimatedAnnualCost=100.0),
        ],
        restrictions=[]
    )
    mock_medicare_client.get_drugs.return_value = mock_drug_info
    mock_drug_alternatives_processor.process_alternatives.return_value = mock_drug_info.alternatives

    response = client.get("/api/drugs/alternatives?plan_id=test_plan&drug_name=TestDrug")

    assert response.status_code == 200
    assert response.json() == [
        {"name": "Alt1", "category": "Generic", "estimatedAnnualCost": 50.0, "plan_id": None},
        {"name": "Alt2", "category": "Brand", "estimatedAnnualCost": 100.0, "plan_id": None},
    ]
    mock_medicare_client.get_drugs.assert_called_once_with("test_plan", "TestDrug")
    mock_drug_alternatives_processor.process_alternatives.assert_called_once_with(mock_drug_info)

def test_get_drug_alternatives_drug_not_found(client, mock_medicare_client):
    mock_medicare_client.get_drugs.return_value = None

    response = client.get("/api/drugs/alternatives?plan_id=test_plan&drug_name=NonExistentDrug")

    assert response.status_code == 404
    assert response.json() == {"detail": "Drug information not found for the given plan and drug to find alternatives."}

def test_get_drug_alternatives_no_alternatives_found(client, mock_medicare_client, mock_drug_alternatives_processor):
    mock_drug_info = DrugInfo(
        drugName="TestDrug",
        alternatives=[],
        restrictions=[]
    )
    mock_medicare_client.get_drugs.return_value = mock_drug_info
    mock_drug_alternatives_processor.process_alternatives.return_value = []

    response = client.get("/api/drugs/alternatives?plan_id=test_plan&drug_name=TestDrug")

    assert response.status_code == 404
    assert response.json() == {"detail": "No drug alternatives found for the given drug."}
