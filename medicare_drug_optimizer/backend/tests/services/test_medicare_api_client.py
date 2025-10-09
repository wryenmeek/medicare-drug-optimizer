# backend/tests/services/test_medicare_api_client.py

import pytest
from unittest.mock import MagicMock, patch
from backend.app.services.medicare_api_client import MedicareAPIClient
from backend.app.models.medicare_api_models import Plan, DrugInfo, DrugAlternative, DrugRestriction, Pharmacy
import requests

@pytest.fixture
def medicare_client():
    return MedicareAPIClient()

@pytest.fixture
def mock_make_request(medicare_client):
    medicare_client._make_request = MagicMock()
    return medicare_client._make_request

# --- Contract Tests for get_plans ---
def test_get_plans_success(medicare_client, mock_make_request):
    # Mock a successful API response
    mock_make_request.return_value = {
        "plans": [
            {"id": "1", "name": "Plan A", "issuer": "Issuer X", "formularyUrl": "http://example.com/a"},
            {"id": "2", "name": "Plan B", "issuer": "Issuer Y", "formularyUrl": "http://example.com/b"},
        ]
    }

    zip_code = "12345"
    county = "SomeCounty"
    plans = medicare_client.get_plans(zip_code, county)

    # Assert that _make_request was called correctly
    mock_make_request.assert_called_once_with("plans", {"zip": zip_code, "county": county})

    # Assert that the returned value is a list of Plan objects
    assert isinstance(plans, list)
    assert len(plans) == 2
    assert all(isinstance(p, Plan) for p in plans)
    assert plans[0].name == "Plan A"
    assert plans[1].issuer == "Issuer Y"

def test_get_plans_api_failure(medicare_client, mock_make_request):
    # Mock an API failure (e.g., _make_request returns None)
    mock_make_request.return_value = None

    zip_code = "12345"
    county = "SomeCounty"
    plans = medicare_client.get_plans(zip_code, county)

    # Assert that _make_request was called correctly
    mock_make_request.assert_called_once_with("plans", {"zip": zip_code, "county": county})

    # Assert that None is returned on API failure
    assert plans is None

def test_get_plans_no_plans_in_response(medicare_client, mock_make_request):
    # Mock an API response that doesn't contain 'plans' key
    mock_make_request.return_value = {"some_other_key": "value"}

    zip_code = "12345"
    county = "SomeCounty"
    plans = medicare_client.get_plans(zip_code, county)

    # Assert that _make_request was called correctly
    mock_make_request.assert_called_once_with("plans", {"zip": zip_code, "county": county})

    # Assert that None is returned if 'plans' key is missing
    assert plans is None

# --- Contract Tests for get_drugs ---
def test_get_drugs_success(medicare_client, mock_make_request):
    # Mock a successful API response for drugs
    mock_make_request.return_value = {
        "drugInfoList": [
            {
                "drugName": "Drug X",
                "alternatives": [
                    {"name": "Alt A", "category": "Generic", "estimatedAnnualCost": 100.0},
                    {"name": "Alt B", "category": "Brand", "estimatedAnnualCost": 200.0},
                ],
                "restrictions": [
                    {"type": "QL", "simplifiedText": "Limit 30 per month", "rawText": "Limit 30 per month"},
                ]
            }
        ]
    }

    plan_id = "PLAN123"
    drug_name = "Drug X"
    drug_info = medicare_client.get_drugs(plan_id, drug_name)

    # Assert that _make_request was called correctly
    mock_make_request.assert_called_once_with("drugs", {"planId": plan_id, "drugName": drug_name})

    # Assert that the returned value is a DrugInfo object
    assert isinstance(drug_info, DrugInfo)
    assert drug_info.drugName == "Drug X"
    assert len(drug_info.alternatives) == 2
    assert isinstance(drug_info.alternatives[0], DrugAlternative)
    assert drug_info.alternatives[0].name == "Alt A"
    assert len(drug_info.restrictions) == 1
    assert isinstance(drug_info.restrictions[0], DrugRestriction)
    assert drug_info.restrictions[0].type == "QL"

def test_get_drugs_api_failure(medicare_client, mock_make_request):
    # Mock an API failure
    mock_make_request.return_value = None

    plan_id = "PLAN123"
    drug_name = "Drug X"
    drug_info = medicare_client.get_drugs(plan_id, drug_name)

    mock_make_request.assert_called_once_with("drugs", {"planId": plan_id, "drugName": drug_name})
    assert drug_info is None

def test_get_drugs_no_drug_info_in_response(medicare_client, mock_make_request):
    # Mock an API response that doesn't contain 'drugInfoList' key
    mock_make_request.return_value = {"some_other_key": "value"}

    plan_id = "PLAN123"
    drug_name = "Drug X"
    drug_info = medicare_client.get_drugs(plan_id, drug_name)

    mock_make_request.assert_called_once_with("drugs", {"planId": plan_id, "drugName": drug_name})
    assert drug_info is None

# --- Contract Tests for get_pharmacies ---
def test_get_pharmacies_success(medicare_client, mock_make_request):
    # Mock a successful API response for pharmacies
    mock_make_request.return_value = {
        "pharmacies": {
            "features": [
                {"properties": {"id": "P1", "name": "Pharmacy 1", "address": "123 Main St", "latitude": 34.0, "longitude": -81.0, "networkStatus": "In-Network"}},
                {"properties": {"id": "P2", "name": "Pharmacy 2", "address": "456 Oak Ave", "latitude": 34.1, "longitude": -81.1, "networkStatus": "Preferred"}},
            ]
        }
    }

    plan_id = "PLAN123"
    zip_code = "12345"
    pharmacies = medicare_client.get_pharmacies(plan_id, zip_code)

    # Assert that _make_request was called correctly
    mock_make_request.assert_called_once_with("pharmacies", {"planId": plan_id, "zip": zip_code})

    # Assert that the returned value is a list of Pharmacy objects
    assert isinstance(pharmacies, list)
    assert len(pharmacies) == 2
    assert all(isinstance(p, Pharmacy) for p in pharmacies)
    assert pharmacies[0].name == "Pharmacy 1"
    assert pharmacies[1].networkStatus == "Preferred"

def test_get_pharmacies_api_failure(medicare_client, mock_make_request):
    # Mock an API failure
    mock_make_request.return_value = None

    plan_id = "PLAN123"
    zip_code = "12345"
    pharmacies = medicare_client.get_pharmacies(plan_id, zip_code)

    mock_make_request.assert_called_once_with("pharmacies", {"planId": plan_id, "zip": zip_code})
    assert pharmacies is None

def test_get_pharmacies_no_pharmacies_in_response(medicare_client, mock_make_request):
    # Mock an API response that doesn't contain 'pharmacies' key
    mock_make_request.return_value = {"some_other_key": "value"}

    plan_id = "PLAN123"
    zip_code = "12345"
    pharmacies = medicare_client.get_pharmacies(plan_id, zip_code)

    mock_make_request.assert_called_once_with("pharmacies", {"planId": plan_id, "zip": zip_code})
    assert pharmacies is None

# --- Unit Tests for _make_request ---
@patch('requests.get')
def test_make_request_success(mock_get, medicare_client):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"data": "test"}
    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response

    endpoint = "test_endpoint"
    params = {"key": "value"}
    result = medicare_client._make_request(endpoint, params)

    mock_get.assert_called_once_with(
        f"{medicare_client.BASE_URL}{endpoint}",
        headers=medicare_client.REFERER_HEADER,
        params=params,
        timeout=10
    )
    assert result == {"data": "test"}

@patch('requests.get')
def test_make_request_http_error(mock_get, medicare_client):
    mock_response = MagicMock()
    mock_response.status_code = 404
    mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError("Not Found")
    mock_get.return_value = mock_response

    endpoint = "test_endpoint"
    result = medicare_client._make_request(endpoint)

    assert result is None

@patch('requests.get')
def test_make_request_timeout_error(mock_get, medicare_client):
    mock_get.side_effect = requests.exceptions.Timeout("Request timed out")

    endpoint = "test_endpoint"
    result = medicare_client._make_request(endpoint)

    assert result is None

# --- Unit Tests for _map_plans ---
def test_map_plans_success(medicare_client):
    raw_data = {
        "plans": [
            {"id": "1", "name": "Plan A", "issuer": "Issuer X", "formularyUrl": "http://example.com/a"},
        ]
    }
    plans = medicare_client._map_plans(raw_data)
    assert isinstance(plans, list)
    assert len(plans) == 1
    assert plans[0].name == "Plan A"

def test_map_plans_empty_data(medicare_client):
    raw_data = {}
    plans = medicare_client._map_plans(raw_data)
    assert plans is None

def test_map_plans_no_plans_key(medicare_client):
    raw_data = {"some_other_key": "value"}
    plans = medicare_client._map_plans(raw_data)
    assert plans is None

# --- Unit Tests for _map_drug_info ---
def test_map_drug_info_success(medicare_client):
    raw_data = {
        "drugInfoList": [
            {
                "drugName": "Drug Y",
                "alternatives": [],
                "restrictions": []
            }
        ]
    }
    drug_info = medicare_client._map_drug_info(raw_data)
    assert isinstance(drug_info, DrugInfo)
    assert drug_info.drugName == "Drug Y"

def test_map_drug_info_empty_data(medicare_client):
    raw_data = {}
    drug_info = medicare_client._map_drug_info(raw_data)
    assert drug_info is None

def test_map_drug_info_no_drug_info_list_key(medicare_client):
    raw_data = {"some_other_key": "value"}
    drug_info = medicare_client._map_drug_info(raw_data)
    assert drug_info is None

# --- Unit Tests for _map_pharmacies ---
def test_map_pharmacies_success(medicare_client):
    raw_data = {
        "pharmacies": {
            "features": [
                {"properties": {"id": "P3", "name": "Pharmacy 3", "address": "789 Pine St", "latitude": 35.0, "longitude": -82.0, "networkStatus": "In-Network"}},
            ]
        }
    }
    pharmacies = medicare_client._map_pharmacies(raw_data)
    assert isinstance(pharmacies, list)
    assert len(pharmacies) == 1
    assert pharmacies[0].name == "Pharmacy 3"

def test_map_pharmacies_empty_data(medicare_client):
    raw_data = {}
    pharmacies = medicare_client._map_pharmacies(raw_data)
    assert pharmacies is None

def test_map_pharmacies_no_pharmacies_key(medicare_client):
    raw_data = {"some_other_key": "value"}
    pharmacies = medicare_client._map_pharmacies(raw_data)
    assert pharmacies is None