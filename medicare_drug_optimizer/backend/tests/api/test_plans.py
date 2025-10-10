import pytest
from fastapi.testclient import TestClient
from unittest.mock import MagicMock
from backend.app.models.medicare_api_models import Plan
from backend.app.api.plans import get_medicare_client

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

def test_get_plans_success(client, mock_medicare_client):
    mock_plans = [
        Plan(id="1", name="Plan A", issuer="Issuer X", formularyUrl="http://example.com/formularyA"),
        Plan(id="2", name="Plan B", issuer="Issuer Y", formularyUrl="http://example.com/formularyB"),
    ]
    mock_medicare_client.get_plans.return_value = mock_plans

    response = client.get("/api/plans?zip_code=12345&county=SomeCounty")

    assert response.status_code == 200
    assert response.json() == [
        {"id": "1", "name": "Plan A", "issuer": "Issuer X", "formulary_url": "http://example.com/formularyA"},
        {"id": "2", "name": "Plan B", "issuer": "Issuer Y", "formulary_url": "http://example.com/formularyB"},
    ]
    mock_medicare_client.get_plans.assert_called_once_with("12345", "SomeCounty")

def test_get_plans_not_found(client, mock_medicare_client):
    mock_medicare_client.get_plans.return_value = None

    response = client.get("/api/plans?zip_code=99999&county=NonExistent")

    assert response.status_code == 404
    assert response.json() == {"detail": "Plans not found for the given zip code and county."}
