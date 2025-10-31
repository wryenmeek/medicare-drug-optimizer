# Data Model

This feature primarily defines the external API structure and how it maps to internal data representations. The internal data models will closely mirror the schemas defined in the provided OpenAPI specification.

## Entities (as defined by Medicare.gov API OpenAPI Specification)

### Plan
Represents a Medicare Part D plan.

- **id**: string
- **name**: string
- **issuer**: string
- **formularyUrl**: string (optional)

### DrugInfo
Represents information about a specific drug, including alternatives and restrictions.

- **drugName**: string
- **alternatives**: array of `DrugAlternative`
- **restrictions**: array of `DrugRestriction`

### DrugAlternative
Represents a covered alternative for a given drug.

- **name**: string
- **category**: string (enum: "Brand", "Generic", "Branded Generic", "Biosimilar", "Interchangeable Biologic")
- **estimatedAnnualCost**: number

### DrugRestriction
Represents a specific rule or requirement applied to a drug by the plan.

- **type**: string (enum: "QL", "PA", "ST")
- **simplifiedText**: string
- **rawText**: string

### Pharmacy
Represents a retail or mail-order pharmacy.

- **id**: string
- **name**: string
- **address**: string
- **latitude**: number
- **longitude**: number
- **networkStatus**: string (enum: "In-Network", "Preferred", "Mail-Order")
