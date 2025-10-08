# backend/tests/api/test_drug_alternatives.py

import pytest
from fastapi.testclient import TestClient
from unittest.mock import MagicMock
from backend.app.main import app, medicare_client, DrugAlternativesProcessor
from backend.app.models.medicare_api_models import DrugInfo, DrugAlternative, DrugRestriction

client = TestClient(app)

@pytest.fixture(autouse=True)
def mock_dependencies():
    medicare_client.get_drugs = MagicMock()
    DrugAlternativesProcessor.process_alternatives = MagicMock()

def test_get_drug_alternatives_success():
    mock_drug_info = DrugInfo(
        drugName="TestDrug",
        alternatives=[
            DrugAlternative(name="Alt1", category="Generic", estimatedAnnualCost=50.0),
            DrugAlternative(name="Alt2", category="Brand", estimatedAnnualCost=100.0),
        ],
        restrictions=[]
    )
    medicare_client.get_drugs.return_value = mock_drug_info
    DrugAlternativesProcessor.process_alternatives.return_value = mock_drug_info.alternatives

    response = client.get("/api/drugs/alternatives?plan_id=test_plan&drug_name=TestDrug")

    assert response.status_code == 200
    assert response.json() == [
        {"name": "Alt1", "category": "Generic", "estimated_annual_cost": 50.0, "plan_id": None},
        {"name": "Alt2", "category": "Brand", "estimated_annual_cost": 100.0, "plan_id": None},
    ]
    medicare_client.get_drugs.assert_called_once_with("test_plan", "TestDrug")
    DrugAlternativesProcessor.process_alternatives.assert_called_once_with(mock_drug_info)

def test_get_drug_alternatives_drug_not_found():
    medicare_client.get_drugs.return_value = None

    response = client.get("/api/drugs/alternatives?plan_id=test_plan&drug_name=NonExistentDrug")

    assert response.status_code == 404
    assert response.json() == {"detail": "Drug information not found for the given plan and drug to find alternatives."
}

def test_get_drug_alternatives_no_alternatives_found():
    mock_drug_info = DrugInfo(
        drugName="TestDrug",
        alternatives=[],
        restrictions=[]
    )
    medicare_client.get_drugs.return_value = mock_drug_info
    DrugAlternativesProcessor.process_alternatives.return_value = []

    response = client.get("/api/drugs/alternatives?plan_id=test_plan&drug_name=TestDrug")

    assert response.status_code == 404
    assert response.json() == {"detail": "No drug alternatives found for the given drug."
}
