# backend/tests/api/test_pharmacy_recommendations.py

import pytest
from fastapi.testclient import TestClient
from unittest.mock import MagicMock
from backend.app.main import app, medicare_client
from backend.app.services.pharmacy_optimizer import PharmacyOptimizer
from backend.app.models.medicare_api_models import Pharmacy
from backend.app.models.user_pharmacy_preferences import UserPharmacyPreferences
from backend.app.models.pharmacy_recommendation import PharmacyRecommendation

client = TestClient(app)

@pytest.fixture(autouse=True)
def mock_dependencies():
    medicare_client.get_pharmacies = MagicMock()
    PharmacyOptimizer.get_recommended_pharmacies = MagicMock()

def test_get_pharmacy_recommendations_success():
    mock_pharmacies = [
        Pharmacy(id="P1", name="Pharmacy 1", address="123 Main St", latitude=34.0, longitude=-81.0, network_status="In-Network"),
    ]
    mock_recommendations = [
        PharmacyRecommendation(pharmacy=mock_pharmacies[0], reason="Closest pharmacy"),
    ]

    medicare_client.get_pharmacies.return_value = mock_pharmacies
    PharmacyOptimizer.get_recommended_pharmacies.return_value = mock_recommendations

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
    medicare_client.get_pharmacies.assert_called_once_with("test_plan", "12345")
    PharmacyOptimizer.get_recommended_pharmacies.assert_called_once()

def test_get_pharmacy_recommendations_no_pharmacies_found():
    medicare_client.get_pharmacies.return_value = None

    response = client.get(
        "/api/pharmacies/recommendations?user_id=test_user&plan_id=test_plan&zip_code=12345&user_latitude=34.0&user_longitude=-81.0"
    )

    assert response.status_code == 404
    assert response.json() == {"detail": "No pharmacies found for the given plan and zip code."}

def test_get_pharmacy_recommendations_no_recommendations_found():
    mock_pharmacies = [
        Pharmacy(id="P1", name="Pharmacy 1", address="123 Main St", latitude=34.0, longitude=-81.0, network_status="In-Network"),
    ]
    medicare_client.get_pharmacies.return_value = mock_pharmacies
    PharmacyOptimizer.get_recommended_pharmacies.return_value = []

    response = client.get(
        "/api/pharmacies/recommendations?user_id=test_user&plan_id=test_plan&zip_code=12345&user_latitude=34.0&user_longitude=-81.0"
    )

    assert response.status_code == 404
    assert response.json() == {"detail": "No pharmacy recommendations found based on your preferences."}
