# backend/app/services/optimization_service.py

from typing import List, Optional
from backend.app.models.partd_plan import PartDPlan
from backend.app.models.drug import Drug
from backend.app.models.pharmacy import Pharmacy
from backend.app.models.fulfillment_plan import FulfillmentPlan

class OptimizationService:
    def __init__(self):
        pass

    def optimize_plans(
        self,
        plans: List[PartDPlan],
        drugs: List[Drug],
        pharmacies: List[Pharmacy]
    ) -> List[FulfillmentPlan]:
        # Placeholder for actual multi-objective optimization logic
        # For now, we'll just return a dummy lowest cost plan, most convenient plan, and least painful plan
        lowest_cost_plan = self._generate_lowest_cost_plan(plans, drugs, pharmacies)
        most_convenient_plan = self._generate_most_convenient_plan(plans, drugs, pharmacies)
        least_painful_plan = self._generate_least_painful_plan(plans, drugs, pharmacies)
        
        results = []
        if lowest_cost_plan:
            results.append(lowest_cost_plan)
        if most_convenient_plan:
            results.append(most_convenient_plan)
        if least_painful_plan:
            results.append(least_painful_plan)
        return results

    def _generate_lowest_cost_plan(
        self,
        plans: List[PartDPlan],
        drugs: List[Drug],
        pharmacies: List[Pharmacy]
    ) -> Optional[FulfillmentPlan]:
        if not plans or not drugs or not pharmacies:
            return None

        # Simple placeholder: assume the first plan and first pharmacy cover all drugs
        # and calculate a dummy cost
        dummy_cost = sum([p.monthly_premium for p in plans]) * 12 + len(drugs) * 50 # Example cost
        
        return FulfillmentPlan(
            plan=plans[0],
            pharmacy=pharmacies[0],
            drugs_covered=drugs,
            estimated_annual_cost=dummy_cost,
            notes="This is a dummy lowest cost plan."
        )

    def _generate_most_convenient_plan(
        self,
        plans: List[PartDPlan],
        drugs: List[Drug],
        pharmacies: List[Pharmacy]
    ) -> Optional[FulfillmentPlan]:
        if not plans or not drugs or not pharmacies:
            return None

        # Simple placeholder: assume the first plan and first pharmacy are most convenient
        dummy_cost = sum([p.monthly_premium for p in plans]) * 12 + len(drugs) * 60 # Slightly higher dummy cost
        
        return FulfillmentPlan(
            plan=plans[0],
            pharmacy=pharmacies[0],
            drugs_covered=drugs,
            estimated_annual_cost=dummy_cost,
            notes="This is a dummy most convenient plan."
        )

    def _generate_least_painful_plan(
        self,
        plans: List[PartDPlan],
        drugs: List[Drug],
        pharmacies: List[Pharmacy]
    ) -> Optional[FulfillmentPlan]:
        if not plans or not drugs or not pharmacies:
            return None

        # Simple placeholder: assume the first plan and first pharmacy are least painful
        dummy_cost = sum([p.monthly_premium for p in plans]) * 12 + len(drugs) * 70 # Slightly higher dummy cost
        
        return FulfillmentPlan(
            plan=plans[0],
            pharmacy=pharmacies[0],
            drugs_covered=drugs,
            estimated_annual_cost=dummy_cost,
            notes="This is a dummy least painful plan."
        )