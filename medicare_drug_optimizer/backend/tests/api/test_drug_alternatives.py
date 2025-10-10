import pytest
from fastapi.testclient import TestClient
from unittest.mock import MagicMock
from app.api.drugs import get_drug_alternatives_service

@pytest.fixture
def mock_drug_alternatives_service():
    return MagicMock()

@pytest.fixture
def client(mock_drug_alternatives_service):
    from app.main import create_app
    app = create_app()
    app.dependency_overrides[get_drug_alternatives_service] = lambda: mock_drug_alternatives_service
    with TestClient(app) as c:
        yield c

def test_get_drug_alternatives_success(client, mock_drug_alternatives_service):
    mock_drug_alternatives_service.get_alternatives.return_value = [
        {"name": "Alt1", "rxcui": "1", "category": "Generic", "tier": "1", "estimated_annual_cost": 50.0},
        {"name": "Alt2", "rxcui": "2", "category": "Brand", "tier": "3", "estimated_annual_cost": 100.0},
    ]

    response = client.get("/api/drugs/12345/alternatives")

    assert response.status_code == 200
    assert response.json() == [
        {"name": "Alt1", "rxcui": "1", "category": "Generic", "tier": "1", "estimated_annual_cost": 50.0},
        {"name": "Alt2", "rxcui": "2", "category": "Brand", "tier": "3", "estimated_annual_cost": 100.0},
    ]
    mock_drug_alternatives_service.get_alternatives.assert_called_once_with("12345")

def test_get_drug_alternatives_not_found(client, mock_drug_alternatives_service):
    mock_drug_alternatives_service.get_alternatives.return_value = None

    response = client.get("/api/drugs/54321/alternatives")

    assert response.status_code == 404
    assert response.json() == {"detail": "No alternatives found for the given drug."}