# backend/tests/api/test_optimized_plans.py

import pytest
from fastapi.testclient import TestClient
from unittest.mock import MagicMock
from backend.app.main import app, medicare_client, OptimizationService
from backend.app.models.medicare_api_models import Plan, Pharmacy
from backend.app.models.partd_plan import PartDPlan
from backend.app.models.drug import Drug
from backend.app.models.fulfillment_plan import FulfillmentPlan

client = TestClient(app)

@pytest.fixture(autouse=True)
def mock_dependencies():
    medicare_client.get_plans = MagicMock()
    medicare_client.get_pharmacies = MagicMock()
    OptimizationService.optimize_plans = MagicMock()

def test_get_optimized_plans_success():
    mock_plans = [
        Plan(id="1", name="Plan A", issuer="Issuer X"),
    ]
    mock_pharmacies = [
        Pharmacy(id="P1", name="Pharmacy 1", address="123 Main St", latitude=34.0, longitude=-81.0, networkStatus="In-Network"),
    ]
    mock_drugs = [
        Drug(drug_name="Drug X"),
    ]
    mock_fulfillment_plan = FulfillmentPlan(
        plan=PartDPlan(plan_id="1", plan_name="Plan A", carrier_name="Issuer X", monthly_premium=10.0, deductible=100.0, out_of_pocket_max=1000.0),
        pharmacy=mock_pharmacies[0],
        drugs_covered=mock_drugs,
        estimated_annual_cost=1000.0,
        notes="Optimized plan"
    )

    medicare_client.get_plans.return_value = mock_plans
    medicare_client.get_pharmacies.return_value = mock_pharmacies
    OptimizationService.optimize_plans.return_value = [mock_fulfillment_plan]

    response = client.get("/api/plans/optimized?zip_code=12345&county=SomeCounty&drug_names=Drug%20X")

    assert response.status_code == 200
    assert response.json() == [
        {
            "plan": {
                "plan_id": "1",
                "plan_name": "Plan A",
                "carrier_name": "Issuer X",
                "monthly_premium": 10.0,
                "deductible": 100.0,
                "out_of_pocket_max": 1000.0,
                "formulary_url": None
            },
            "pharmacy": {
                "id": "P1",
                "name": "Pharmacy 1",
                "address": "123 Main St",
                "latitude": 34.0,
                "longitude": -81.0,
                "network_status": "In-Network",
                "distance": None
            },
            "drugs_covered": [
                {"drug_name": "Drug X", "ndc_code": None, "dosage": None, "quantity": None, "frequency": None}
            ],
            "estimated_annual_cost": 1000.0,
            "notes": "Optimized plan"
        }
    ]
    medicare_client.get_plans.assert_called_once_with("12345", "SomeCounty")
    medicare_client.get_pharmacies.assert_called_once_with(mock_plans[0].id, "12345")
    OptimizationService.optimize_plans.assert_called_once()

def test_get_optimized_plans_no_plans_found():
    medicare_client.get_plans.return_value = None

    response = client.get("/api/plans/optimized?zip_code=12345&county=SomeCounty&drug_names=Drug%20X")

    assert response.status_code == 404
    assert response.json() == {"detail": "No plans found for the given zip code and county."}

def test_get_optimized_plans_no_pharmacies_found():
    mock_plans = [
        Plan(id="1", name="Plan A", issuer="Issuer X"),
    ]
    medicare_client.get_plans.return_value = mock_plans
    medicare_client.get_pharmacies.return_value = None

    response = client.get("/api/plans/optimized?zip_code=12345&county=SomeCounty&drug_names=Drug%20X")

    assert response.status_code == 404
    assert response.json() == {"detail": "No pharmacies found for the given plan and zip code."}

def test_get_optimized_plans_no_optimized_plans_found():
    mock_plans = [
        Plan(id="1", name="Plan A", issuer="Issuer X"),
    ]
    mock_pharmacies = [
        Pharmacy(id="P1", name="Pharmacy 1", address="123 Main St", latitude=34.0, longitude=-81.0, networkStatus="In-Network"),
    ]
    medicare_client.get_plans.return_value = mock_plans
    medicare_client.get_pharmacies.return_value = mock_pharmacies
    OptimizationService.optimize_plans.return_value = []

    response = client.get("/api/plans/optimized?zip_code=12345&county=SomeCounty&drug_names=Drug%20X")

    assert response.status_code == 404
    assert response.json() == {"detail": "No optimized plans found."}
