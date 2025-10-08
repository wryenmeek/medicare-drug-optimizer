# backend/tests/services/test_optimization_service.py

import pytest
from backend.app.services.optimization_service import OptimizationService
from backend.app.models.partd_plan import PartDPlan
from backend.app.models.drug import Drug
from backend.app.models.pharmacy import Pharmacy
from backend.app.models.fulfillment_plan import FulfillmentPlan

@pytest.fixture
def optimization_service():
    return OptimizationService()

@pytest.fixture
def sample_data():
    plans = [
        PartDPlan(plan_id="P1", plan_name="Plan A", carrier_name="C1", monthly_premium=10.0, deductible=100.0, out_of_pocket_max=1000.0),
        PartDPlan(plan_id="P2", plan_name="Plan B", carrier_name="C2", monthly_premium=15.0, deductible=50.0, out_of_pocket_max=1200.0),
    ]
    drugs = [
        Drug(drug_name="Drug X"),
        Drug(drug_name="Drug Y"),
    ]
    pharmacies = [
        Pharmacy(id="PH1", name="Pharmacy 1", address="Addr1", latitude=1.0, longitude=1.0, network_status="In-Network"),
        Pharmacy(id="PH2", name="Pharmacy 2", address="Addr2", latitude=2.0, longitude=2.0, network_status="Preferred"),
    ]
    return plans, drugs, pharmacies

def test_optimize_plans_returns_list_of_fulfillment_plans(optimization_service, sample_data):
    plans, drugs, pharmacies = sample_data
    optimized_plans = optimization_service.optimize_plans(plans, drugs, pharmacies)
    assert isinstance(optimized_plans, list)
    assert all(isinstance(p, FulfillmentPlan) for p in optimized_plans)

def test_generate_lowest_cost_plan(optimization_service, sample_data):
    plans, drugs, pharmacies = sample_data
    lowest_cost_plan = optimization_service._generate_lowest_cost_plan(plans, drugs, pharmacies)
    assert lowest_cost_plan is not None
    assert lowest_cost_plan.notes == "This is a dummy lowest cost plan."

def test_generate_most_convenient_plan(optimization_service, sample_data):
    plans, drugs, pharmacies = sample_data
    most_convenient_plan = optimization_service._generate_most_convenient_plan(plans, drugs, pharmacies)
    assert most_convenient_plan is not None
    assert most_convenient_plan.notes == "This is a dummy most convenient plan."

def test_generate_least_painful_plan(optimization_service, sample_data):
    plans, drugs, pharmacies = sample_data
    least_painful_plan = optimization_service._generate_least_painful_plan(plans, drugs, pharmacies)
    assert least_painful_plan is not None
    assert least_painful_plan.notes == "This is a dummy least painful plan."

def test_optimize_plans_empty_inputs(optimization_service):
    assert optimization_service.optimize_plans([], [], []) == []
    assert optimization_service._generate_lowest_cost_plan([], [], []) is None
    assert optimization_service._generate_most_convenient_plan([], [], []) is None
    assert optimization_service._generate_least_painful_plan([], [], []) is None
