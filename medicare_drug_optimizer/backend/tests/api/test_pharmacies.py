import pytest
from fastapi.testclient import TestClient
from unittest.mock import MagicMock
from backend.app.models.medicare_api_models import Pharmacy
from backend.app.api.pharmacies import get_medicare_client

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

def test_get_pharmacies_success(client, mock_medicare_client):
    mock_pharmacies = [
        Pharmacy(id="P1", name="Pharmacy 1", address="123 Main St", latitude=34.0, longitude=-81.0, networkStatus="In-Network"),
        Pharmacy(id="P2", name="Pharmacy 2", address="456 Oak Ave", latitude=34.1, longitude=-81.1, networkStatus="Preferred"),
    ]
    mock_medicare_client.get_pharmacies.return_value = mock_pharmacies

    response = client.get("/api/pharmacies?plan_id=test_plan&zip_code=12345")

    assert response.status_code == 200
    assert response.json() == [
        {"id": "P1", "name": "Pharmacy 1", "address": "123 Main St", "latitude": 34.0, "longitude": -81.0, "networkStatus": "In-Network"},
        {"id": "P2", "name": "Pharmacy 2", "address": "456 Oak Ave", "latitude": 34.1, "longitude": -81.1, "networkStatus": "Preferred"},
    ]
    mock_medicare_client.get_pharmacies.assert_called_once_with("test_plan", "12345")

def test_get_pharmacies_not_found(client, mock_medicare_client):
    mock_medicare_client.get_pharmacies.return_value = None

    response = client.get("/api/pharmacies?plan_id=test_plan&zip_code=99999")

    assert response.status_code == 404
    assert response.json() == {"detail": "Pharmacies not found for the given plan and zip code."}
