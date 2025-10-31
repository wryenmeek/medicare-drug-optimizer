# Feature Specification: Drug Coverage Details and Restrictions

**Feature Branch**: `003-once-we-have`  
**Created**: 2025-10-06  
**Status**: Draft  
**Input**: User description: "once we have all the possible covered alternatives, I'd like the application to help me understand how my plan covers the alternatives across different packages, dosages, and refil frequency intervals. I'd also like the application to help me understand the quantity limits and other restrictions my plan may put on each drug."

---

## Clarifications

### Session 2025-10-06
- **Q**: When the system encounters a complex restriction on a drug (e.g., "Step Therapy: Must try Drug X and Drug Y first"), how should it present this information?
- **A**: Attempt to Simplify (The system should try to parse the rule and present it as a simple checklist or a summarized sentence).

---

## ⚡ Quick Guidelines
- ✅ Focus on WHAT users need and WHY
- ❌ Avoid HOW to implement (no tech stack, APIs, code structure)
- 👥 Written for business stakeholders, not developers

---

## User Scenarios & Testing *(mandatory)*

### Primary User Story
As a Medicare beneficiary, after finding covered alternatives for my drugs, I want to understand the specific coverage details for each alternative, including how different dosages or package sizes are covered, and what limits or restrictions my plan imposes.

### Acceptance Scenarios
1. **Given** a user is viewing a covered drug alternative, **When** they select it for more details, **Then** the system displays its comprehensive coverage information.
2. **Given** the coverage information is displayed, **Then** it clearly lists how the plan covers different package sizes, dosages, and refill frequencies (e.g., 30-day vs. 90-day supply).
3. **Given** the coverage information is displayed, **Then** it explicitly states any utilization management restrictions, such as Quantity Limits (QL), Prior Authorization (PA), or Step Therapy (ST).

### Edge Cases
- What does the system display if the plan's formulary data does not differentiate coverage for various dosages or package sizes?
- Complex restrictions (e.g., Step Therapy) should be parsed and simplified into a checklist or summary sentence for the user.
- What is the fallback if detailed restriction information is not available through the data source?

## Requirements *(mandatory)*

### Functional Requirements
- **FR-001**: For any given covered drug (whether an original or an alternative), the system MUST retrieve and display its detailed coverage rules from the plan's formulary.
- **FR-002**: The system MUST show how coverage and cost may change based on different dosages, package sizes, and refill intervals (e.g., 30-day vs. 90-day supply).
- **FR-003**: The system MUST identify any utilization management restrictions (QL, PA, ST) and, where possible, parse and simplify the specific rules into a checklist or summary sentence for the user.
- **FR-004**: The system MUST provide simple, user-friendly explanations for what each type of restriction (QL, PA, ST) means for the user.
- **FR-005**: The system MUST clearly indicate when specific coverage details or restrictions are not available or not applicable for a selected drug.

### Key Entities *(include if feature involves data)*
- **User**: The Medicare beneficiary.
- **PartDPlan**: The user's prescription drug plan.
- **Drug/DrugAlternative**: The specific medication being investigated.
- **CoverageDetails**: A set of information for a specific drug, detailing how different formulations (dosage, package size) are covered by the plan.
- **UtilizationRestriction**: A specific rule or requirement applied to a drug by the plan, such as a Quantity Limit, a Prior Authorization requirement, or a Step Therapy protocol.

---

## Review & Acceptance Checklist
*GATE: To be reviewed before planning phase*

### Content Quality
- [ ] No implementation details (languages, frameworks, APIs)
- [ ] Focused on user value and business needs
- [ ] Written for non-technical stakeholders
- [ ] All mandatory sections completed

### Requirement Completeness
- [ ] No [NEEDS CLARIFICATION] markers remain
- [ ] Requirements are testable and unambiguous  
- [ ] Success criteria are measurable
- [ ] Scope is clearly bounded
- [ ] Dependencies and assumptions identified

---