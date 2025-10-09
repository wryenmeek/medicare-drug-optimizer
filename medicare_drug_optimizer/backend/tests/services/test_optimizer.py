# backend/tests/services/test_optimizer.py

import pytest
from backend.app.services.optimizer import DrugOptimizer
from backend.app.models.partd_plan import PartDPlan
from backend.app.models.drug import Drug
from backend.app.models.recommendation import Recommendation

def test_optimizer_initialization():
    optimizer = DrugOptimizer()
    assert isinstance(optimizer, DrugOptimizer)

def test_optimize_costs_returns_empty_list_initially():
    optimizer = DrugOptimizer()
    plans = [PartDPlan(plan_id="P1", plan_name="Plan A", carrier_name="C1", monthly_premium=10.0, deductible=100.0, out_of_pocket_max=1000.0)]
    drugs = [Drug(drug_name="Drug X")]
    recommendations = optimizer.optimize_costs(plans, drugs)
    assert isinstance(recommendations, list)
    assert len(recommendations) == 0

# More comprehensive tests will be added as optimization logic is implemented
