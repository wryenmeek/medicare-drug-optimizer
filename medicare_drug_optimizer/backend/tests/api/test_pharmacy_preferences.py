# backend/tests/api/test_pharmacy_preferences.py

import pytest
from fastapi.testclient import TestClient
from unittest.mock import MagicMock
from backend.app.main import app
from backend.app.api.pharmacies import user_pharmacy_preferences_db
from backend.app.models.user_pharmacy_preferences import UserPharmacyPreferences

client = TestClient(app)

@pytest.fixture(autouse=True)
def clear_db():
    user_pharmacy_preferences_db.clear()

def test_get_pharmacy_preferences_default():
    user_id = "test_user"
    response = client.get(f"/api/pharmacies/preferences?user_id={user_id}")

    assert response.status_code == 200
    assert response.json() == {
        "preferred_pharmacy_ids": [],
        "max_travel_distance": None,
        "allow_mail_order": False
    }

def test_get_pharmacy_preferences_existing():
    user_id = "test_user"
    preferences = UserPharmacyPreferences(
        preferred_pharmacy_ids=["P1", "P2"],
        max_travel_distance=10.0,
        allow_mail_order=True
    )
    user_pharmacy_preferences_db[user_id] = preferences

    response = client.get(f"/api/pharmacies/preferences?user_id={user_id}")

    assert response.status_code == 200
    assert response.json() == preferences.model_dump()
def test_update_pharmacy_preferences():
    user_id = "test_user"
    preferences_data = {
        "preferred_pharmacy_ids": ["P3"],
        "max_travel_distance": 5.0,
        "allow_mail_order": False
    }
    response = client.post(f"/api/pharmacies/preferences?user_id={user_id}", json=preferences_data)

    assert response.status_code == 200
    assert response.json() == preferences_data
    assert user_pharmacy_preferences_db[user_id].preferred_pharmacy_ids == ["P3"]
