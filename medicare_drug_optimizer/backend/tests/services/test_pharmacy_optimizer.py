# backend/tests/services/test_pharmacy_optimizer.py

import pytest
from backend.app.services.pharmacy_optimizer import PharmacyOptimizer
from backend.app.models.pharmacy import Pharmacy
from backend.app.models.user_pharmacy_preferences import UserPharmacyPreferences
from backend.app.models.pharmacy_recommendation import PharmacyRecommendation

def test_optimizer_initialization():
    optimizer = PharmacyOptimizer()
    assert isinstance(optimizer, PharmacyOptimizer)

def test_get_recommended_pharmacies_returns_all_pharmacies_by_default():
    optimizer = PharmacyOptimizer()
    all_pharmacies = [
        Pharmacy(id="P1", name="Pharmacy 1", address="123 Main St", latitude=34.0, longitude=-81.0, network_status="In-Network"),
        Pharmacy(id="P2", name="Pharmacy 2", address="456 Oak Ave", latitude=34.1, longitude=-81.1, network_status="Preferred"),
    ]
    user_preferences = UserPharmacyPreferences()
    user_latitude = 34.05
    user_longitude = -81.05

    recommendations = optimizer.get_recommended_pharmacies(
        all_pharmacies, user_preferences, user_latitude, user_longitude
    )

    assert isinstance(recommendations, list)
    assert len(recommendations) == 2
    assert all(isinstance(r, PharmacyRecommendation) for r in recommendations)
    assert recommendations[0].pharmacy.id == "P1"
    assert recommendations[1].pharmacy.id == "P2"

# More comprehensive tests will be added as optimization logic is implemented
