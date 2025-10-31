# Data Model

This feature introduces new entities to represent the generated fulfillment plans and their comparisons.

## Entities

### FulfillmentPlan
Represents a complete, actionable plan for a user to get their prescriptions, optimized according to specific criteria.

- **plan_id**: Unique identifier for the fulfillment plan.
- **type**: The type of plan (e.g., "Lowest Cost", "Most Convenient", "Least Painful").
- **total_annual_cost**: The estimated total annual cost for all drugs in this plan.
- **total_annual_savings**: The estimated annual savings compared to the user's current setup.
- **drug_selections**: A list of objects, each specifying a `Drug` (or `DrugAlternative`) and its selected `Pharmacy` for this plan.
- **pharmacy_selections**: A list of `Pharmacy` objects used in this plan.
- **tradeoffs_description**: A brief description of the tradeoffs associated with this plan (e.g., "Requires visiting two pharmacies").

### PlanComparison
Represents a summary that highlights the key differences and tradeoffs between two or more generated Fulfillment Plans.

- **comparison_id**: Unique identifier for the comparison.
- **plan_ids**: A list of `plan_id`s being compared.
- **comparison_details**: A structured description of the differences, focusing on cost, convenience, and complexity.
