# Prompt Use Cases

## Code Quality
- **Refactoring**
  - **Goal**: Improve readability and performance
  - **Input**: Source function in [LANGUAGE]
  - **Output**: Optimized code + explanation

- **Style Enforcement**
  - **Goal**: Enforce consistent naming and formatting
  - **Input**: Code block
  - **Output**: Rewritten code with consistent style

- **Architecture Review**
  - **Goal**: Identify design pattern violations and code smells
  - **Input**: Class or module structure
  - **Output**: Architectural feedback + structural improvements

## Debugging
- **Error Log Analysis**
  - **Goal**: Identify root cause of runtime errors or stack traces
  - **Input**: Stack trace + execution context
  - **Output**: Root cause explanation + fix recommendation

- **Bug Fixing**
  - **Goal**: Locate and resolve logic bugs in failing functions
  - **Input**: Buggy code snippet + expected behavior
  - **Output**: Corrected code + line-by-line explanation

- **Edge Case Detection**
  - **Goal**: Find unhandled edge cases or boundary conditions
  - **Input**: Target function logic
  - **Output**: List of vulnerable edge cases + defensive code patches

## Documentation
- **API Documentation**
  - **Goal**: Generate comprehensive OpenAPI/JSDoc function docs
  - **Input**: Function signature + parameters
  - **Output**: Formatted docstrings with param/return types

- **README Generation**
  - **Goal**: Produce project landing documentation and setup guide
  - **Input**: Project structure + tech stack details
  - **Output**: Markdown README with installation & usage instructions

- **Code Explanation**
  - **Goal**: Explain complex codebase logic for onboarding engineers
  - **Input**: Complex algorithm code block
  - **Output**: Step-by-step plain English breakdown

## Testing
- **Unit Test Generation**
  - **Goal**: Create automated unit tests with high boundary coverage
  - **Input**: Source function + testing framework (e.g., Jest, PyTest)
  - **Output**: Complete test suite with mock assertions

- **Integration Test Scenarios**
  - **Goal**: Design multi-component integration workflow tests
  - **Input**: API routes + database interaction patterns
  - **Output**: End-to-end testing script structure
