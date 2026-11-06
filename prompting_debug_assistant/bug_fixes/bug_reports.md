## Bug Report - bug1.py
- **Summary**: Off-by-one error in loop boundary conditions.
- **Root Cause**: The range function used `n + 1` instead of `n`, causing index out of bounds exceptions.
- **Resolution**: Changed implementation to use safe Python negative slicing `items[-n:]` (AI suggestion + manual slice adjustment).
- **Lesson Learned**: Always verify loop boundaries and prefer built-in slicing mechanisms for collection extractions.

## Bug Report - bug2.js
- **Summary**: Logical error / Out of bounds iteration in JavaScript array processing.
- **Root Cause**: Loop condition used `<=` instead of `<` when checking `cartItems.length`, attempting to read undefined properties.
- **Resolution**: Updated loop condition to `<` and added property existence checks (AI suggestion).
- **Lesson Learned**: Ensure array iteration bounds strictly stay below array length to prevent undefined access.

## Bug Report - bug3.py
- **Summary**: Runtime exception due to missing format validation.
- **Root Cause**: Assumed comma-separated string always contained expected indices without length checks, triggering IndexError.
- **Resolution**: Added input validation, string existence checks, and `try-except` blocks (AI suggestion + manual validation).
- **Lesson Learned**: Always validate external data formats and lengths before parsing or unpacking.

## Bug Report - bug4.js
- **Summary**: Data type misuse leading to potential calculation errors.
- **Root Cause**: Inputs passed as strings caused unintended behavior during arithmetic operations.
- **Resolution**: Added explicit numeric parsing using `parseFloat()` and `isNaN()` validation (AI suggestion).
- **Lesson Learned**: Enforce strict type checking and explicit conversion for numerical inputs.

## Bug Report - bug5.c
- **Summary**: Buffer over-read / Off-by-one error in C array summation.
- **Root Cause**: Loop condition ran up to `i <= size` instead of `i < size`, accessing memory outside the allocated array bounds.
- **Resolution**: Corrected loop condition to `i < size` (AI suggestion).
- **Lesson Learned**: Pay close attention to C array pointer bounds to avoid segmentation faults and buffer over-reads.
