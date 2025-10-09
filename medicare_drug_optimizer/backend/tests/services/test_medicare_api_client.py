import pytest
import requests
from unittest.mock import MagicMock, patch
from backend.app.services.medicare_api_client import MedicareAPIClient
from backend.app.models.medicare_api_models import Plan, DrugInfo, DrugAlternative, DrugRestriction, Pharmacy

@pytest.fixture
def mock_response():
    with patch('requests.get') as mock_get:
        yield mock_get

@pytest.fixture
def client():
    return MedicareAPIClient()

def test_get_plans_success(client, mock_response):
    mock_response.return_value.status_code = 200
    mock_response.return_value.json.return_value = {
        "plans": [
            {"id": "1", "name": "Plan A", "issuer": "Issuer X", "formularyUrl": "http://example.com/formularyA"},
        ]
    }
    plans = client.get_plans("12345", "SomeCounty")
    assert len(plans) == 1
    assert plans[0].id == "1"
    mock_response.assert_called_once_with(
        f"{client.BASE_URL}plans",
        params={'zip': "12345", 'county': "SomeCounty"},
        headers=client.HEADERS,
        timeout=10
    )

def test_get_plans_not_found(client, mock_response):
    mock_response.return_value.status_code = 200
    mock_response.return_value.json.return_value = {"plans": []}
    plans = client.get_plans("99999", "NonExistent")
    assert plans == []

def test_get_plans_api_error(client, mock_response):
    mock_response.return_value.status_code = 500
    mock_response.return_value.raise_for_status.side_effect = requests.exceptions.HTTPError
    plans = client.get_plans("12345", "SomeCounty")
    assert plans is None

def test_get_drugs_success(client, mock_response):
    mock_response.return_value.status_code = 200
    mock_response.return_value.json.return_value = {
        "drugInfoList": [
            {
                "drugName": "TestDrug",
                "alternatives": [],
                "restrictions": []
            }
        ]
    }
    drug_info = client.get_drugs("test_plan", "TestDrug")
    assert drug_info.drugName == "TestDrug"

def test_get_drugs_not_found(client, mock_response):
    mock_response.return_value.status_code = 200
    mock_response.return_value.json.return_value = {"drugInfoList": []}
    drug_info = client.get_drugs("test_plan", "NonExistentDrug")
    assert drug_info is None

def test_get_pharmacies_success(client, mock_response):
    mock_response.return_value.status_code = 200
    mock_response.return_value.json.return_value = {
        "pharmacies": [
            {"id": "P1", "name": "Pharmacy 1", "address": "123 Main St", "latitude": 34.0, "longitude": -81.0, "networkStatus": "In-Network"},
        ]
    }
    pharmacies = client.get_pharmacies("test_plan", "12345")
    assert len(pharmacies) == 1
    assert pharmacies[0].id == "P1"
