import pytest
from fastapi.testclient import TestClient
from unittest.mock import MagicMock
from backend.app.models.pharmacy import Pharmacy
from backend.app.models.user_pharmacy_preferences import UserPharmacyPreferences
from backend.app.models.pharmacy_recommendation import PharmacyRecommendation
from backend.app.api.pharmacies import get_medicare_client, get_pharmacy_optimizer

@pytest.fixture
def mock_medicare_client():
    return MagicMock()

@pytest.fixture
def mock_pharmacy_optimizer():
    return MagicMock()

@pytest.fixture
def client(mock_medicare_client, mock_pharmacy_optimizer):
    from backend.app.main import create_app
    app = create_app()
    app.dependency_overrides[get_medicare_client] = lambda: mock_medicare_client
    app.dependency_overrides[get_pharmacy_optimizer] = lambda: mock_pharmacy_optimizer
    with TestClient(app) as c:
        yield c

def test_get_pharmacy_recommendations_success(client, mock_medicare_client, mock_pharmacy_optimizer):
    mock_pharmacies = [
        Pharmacy(id="P1", name="Pharmacy 1", address="123 Main St", latitude=34.0, longitude=-81.0, network_status="In-Network"),
    ]
    mock_recommendations = [
        PharmacyRecommendation(pharmacy=mock_pharmacies[0], reason="Closest pharmacy"),
    ]

    mock_medicare_client.get_pharmacies.return_value = mock_pharmacies
    mock_pharmacy_optimizer.get_recommended_pharmacies.return_value = mock_recommendations

    response = client.get(
        "/api/pharmacies/recommendations?user_id=test_user&plan_id=test_plan&zip_code=12345&user_latitude=34.0&user_longitude=-81.0"
    )

    assert response.status_code == 200
    assert response.json() == [
        {
            "pharmacy": {
                "id": "P1",
                "name": "Pharmacy 1",
                "address": "123 Main St",
                "latitude": 34.0,
                "longitude": -81.0,
                "network_status": "In-Network",
                "distance": None
            },
            "reason": "Closest pharmacy",
            "estimated_cost_impact": None
        }
    ]
    mock_medicare_client.get_pharmacies.assert_called_once_with("test_plan", "12345")
    mock_pharmacy_optimizer.get_recommended_pharmacies.assert_called_once()

def test_get_pharmacy_recommendations_no_pharmacies_found(client, mock_medicare_client):
    mock_medicare_client.get_pharmacies.return_value = None

    response = client.get(
        "/api/pharmacies/recommendations?user_id=test_user&plan_id=test_plan&zip_code=12345&user_latitude=34.0&user_longitude=-81.0"
    )

    assert response.status_code == 404
    assert response.json() == {"detail": "No pharmacies found for the given plan and zip code."}

def test_get_pharmacy_recommendations_no_recommendations_found(client, mock_medicare_client, mock_pharmacy_optimizer):
    mock_pharmacies = [
        Pharmacy(id="P1", name="Pharmacy 1", address="123 Main St", latitude=34.0, longitude=-81.0, network_status="In-Network"),
    ]
    mock_medicare_client.get_pharmacies.return_value = mock_pharmacies
    mock_pharmacy_optimizer.get_recommended_pharmacies.return_value = []

    response = client.get(
        "/api/pharmacies/recommendations?user_id=test_user&plan_id=test_plan&zip_code=12345&user_latitude=34.0&user_longitude=-81.0"
    )

    assert response.status_code == 404
    assert response.json() == {"detail": "No pharmacy recommendations found based on your preferences."}
