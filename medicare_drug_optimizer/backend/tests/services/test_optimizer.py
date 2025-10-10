import pytest
from backend.app.services.optimizer import OptimizationService
from backend.app.models.partd_plan import PartDPlan
from backend.app.models.drug import Drug
from backend.app.models.medicare_api_models import Pharmacy
from backend.app.models.fulfillment_plan import FulfillmentPlan
from backend.app.models.recommendation import Recommendation

@pytest.fixture
def optimization_service():
    return OptimizationService()

@pytest.fixture
def sample_data():
    plans = [
        PartDPlan(plan_id="P1", plan_name="Plan A", carrier_name="C1", monthly_premium=10.0, deductible=100.0, out_of_pocket_max=1000.0),
        PartDPlan(plan_id="P2", plan_name="Plan B", carrier_name="C2", monthly_premium=20.0, deductible=50.0, out_of_pocket_max=1200.0),
    ]
    drugs = [
        Drug(drug_name="DrugX", dosage="10mg", quantity=30, frequency="monthly"),
        Drug(drug_name="DrugY", dosage="5mg", quantity=60, frequency="monthly"),
    ]
    pharmacies = [
        Pharmacy(id="PH1", name="Pharmacy 1", address="Addr1", latitude=1.0, longitude=1.0, networkStatus="In-Network"),
        Pharmacy(id="PH2", name="Pharmacy 2", address="Addr2", latitude=2.0, longitude=2.0, networkStatus="Preferred"),
    ]
    return plans, drugs, pharmacies

def test_optimize_plans_returns_list_of_fulfillment_plans(optimization_service, sample_data):
    plans, drugs, pharmacies = sample_data
    optimized_plans = optimization_service.optimize_plans(plans, drugs, pharmacies)
    assert isinstance(optimized_plans, list)
    assert len(optimized_plans) > 0
    assert all(isinstance(p, FulfillmentPlan) for p in optimized_plans)

def test_optimize_plans_empty_inputs(optimization_service):
    assert optimization_service.optimize_plans([], [], []) == []

def test_get_recommendations_returns_list_of_recommendations(optimization_service, sample_data):
    plans, drugs, pharmacies = sample_data
    fulfillment_plan = FulfillmentPlan(
        plan=plans[0],
        pharmacy=pharmacies[0],
        drugs_covered=drugs,
        estimated_annual_cost=1000.0,
        notes="Test notes"
    )
    recommendations = optimization_service.get_recommendations(fulfillment_plan)
    assert isinstance(recommendations, list)
    assert len(recommendations) > 0
    assert all(isinstance(r, Recommendation) for r in recommendations)