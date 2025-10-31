# Data Model

This feature introduces new entities to represent detailed drug coverage information and utilization restrictions.

## Entities

### CoverageDetails
Represents how a specific drug (or alternative) is covered by the plan, considering different formulations.

- **drug_rxcui**: The RxNorm Concept Unique Identifier for the drug.
- **plan_id**: The ID of the Part D plan.
- **dosage**: The specific dosage (e.g., "20mg").
- **package_size**: The size of the drug package (e.g., "30 tablets").
- **refill_frequency**: The allowed refill interval (e.g., "30-day", "90-day").
- **estimated_annual_cost**: The estimated annual cost for this specific formulation.
- **tier**: The formulary tier for this formulation.

### UtilizationRestriction
Represents a specific rule or requirement applied to a drug by the plan.

- **drug_rxcui**: The RxNorm Concept Unique Identifier for the drug.
- **plan_id**: The ID of the Part D plan.
- **type**: The type of restriction (e.g., "QL" for Quantity Limit, "PA" for Prior Authorization, "ST" for Step Therapy).
- **simplified_text**: A user-friendly, parsed, and simplified explanation of the restriction (e.g., "Requires you to try Drug X first").
- **raw_text**: The original, official text of the restriction from the formulary data.
