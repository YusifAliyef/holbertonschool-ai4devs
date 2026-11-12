## Task 1 - CRUD Endpoint
**Requirements**: Implement POST /users with validation.
**Inputs**: JSON {name, email}
**Outputs**: Stored user with ID
**Acceptance Criteria**:
- Returns 201 on success
- Returns 400 on invalid email

## Task 2 - Data Filtering API
**Requirements**: Implement GET /products with query parameters for price filtering.
**Inputs**: Query params {min_price, max_price}
**Outputs**: Filtered JSON array of products
**Acceptance Criteria**:
- Returns matching products within range
- Returns 400 if min_price > max_price

## Task 3 - Input Validation Middleware
**Requirements**: Create a middleware to sanitize user input fields.
**Inputs**: Request body with raw text strings
**Outputs**: Sanitized request body
**Acceptance Criteria**:
- Strips HTML tags from string fields
- Passes control to next middleware on success
