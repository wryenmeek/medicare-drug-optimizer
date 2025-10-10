# Data Model

This feature is primarily session-based and does not require a persistent database for user data. The data model describes the key objects that will be used during an active user session.

## Entities

### UserSession

Represents a single user's journey through the optimization process.

- **session_id**: A unique identifier for the session.
- **part_d_plan**: The PartDPlan object selected by the user.
- **drug_list**: A list of Drug objects entered by the user.

### PartDPlan

Represents a Medicare Part D plan.

- **plan_id**: The official ID of the plan from medicare.gov.
- **plan_name**: The display name of the plan.
- **issuer**: The name of the insurance company.
- **formulary_url**: (Optional) A direct link to the plan's formulary document.

### Drug

Represents a single medication.

- **drug_name**: The name of the drug (e.g., "Lisinopril").
- **dosage**: The dosage of the medication (e.g., "20mg").
- **quantity**: The number of units per refill (e.g., "90").
- **frequency**: The refill frequency (e.g., "monthly", "90-day").

### Recommendation

Represents a single actionable suggestion for cost savings.

- **recommendation_type**: The type of recommendation (e.g., "SWITCH_TO_GENERIC", "USE_PREFERRED_PHARMACY").
- **description**: A user-friendly explanation of the recommendation.
- **estimated_savings**: The estimated annual savings for this specific action.
