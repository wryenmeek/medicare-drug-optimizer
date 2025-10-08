# Data Model

This feature primarily defines the frontend's architectural structure and its dependencies on design systems. It does not introduce new backend data models.

## Entities

### FrontendApplication
Represents the Single Page Application (SPA) itself.

- **architecture**: SPA
- **framework**: React (or similar modern JavaScript framework)
- **design_system_primary**: `ds-medicare-gov`
- **design_system_fallback**: Main CMS Design System library

### UIComponent
Represents a user interface component within the SPA.

- **name**: Name of the component (e.g., "Button", "FormInput").
- **source**: Where the component is sourced from (e.g., "ds-medicare-gov", "CMS-design-system", "Custom").
- **adherence_to_principles**: Boolean, indicates if custom components adhere to design system principles.
