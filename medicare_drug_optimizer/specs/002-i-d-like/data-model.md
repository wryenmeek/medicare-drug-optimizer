# Data Model

This feature extends the existing data model by formalizing the `DrugAlternative` entity, which was introduced in the feature specification.

## Entities

### DrugAlternative
Represents a covered alternative for a given drug on the user's list. This object is a child of the `Drug` entity.

- **rxcui**: The RxNorm Concept Unique Identifier for the alternative drug.
- **name**: The display name of the alternative drug.
- **category**: The category of the alternative, as defined in the spec (e.g., "Generic", "Brand", "Biosimilar").
- **formulary_status**: The status of the drug on the user's plan (e.g., "Covered", "Not Covered").
- **tier**: The drug's tier on the plan's formulary.
- **estimated_annual_cost**: The estimated annual cost for this drug, as calculated by medicare.gov.