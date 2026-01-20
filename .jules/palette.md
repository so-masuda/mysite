## 2024-07-25 - Hardcoded Validation Rules

**Learning:** Hardcoding validation rules in templates creates a maintainability issue. If the backend validation logic changes, the frontend must be updated manually, otherwise the user will see outdated requirements.

**Action:** When possible, dynamically generate validation messages from the backend form validators. If this is not possible, create a follow-up task to address the technical debt.
