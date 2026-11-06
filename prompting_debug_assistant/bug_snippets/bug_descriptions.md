## Bug 1 - bug1.py
**Intended Behavior**: Return the last n items of a list.
**Issue Type**: Off-by-one error.
**Notes**: The loop goes out of bounds when index calculation is incorrect.

## Bug 2 - bug2.js
**Intended Behavior**: Calculate total price of cart items.
**Issue Type**: Logical error / Out of bounds.
**Notes**: Iterating past array length causes TypeError on undefined property.

## Bug 3 - bug3.py
**Intended Behavior**: Parse comma-separated user data string.
**Issue Type**: Runtime exception (IndexError).
**Notes**: Fails when expected format or index is missing.

## Bug 4 - bug4.js
**Intended Behavior**: Subtract discount from given price.
**Issue Type**: Misuse of data types.
**Notes**: Fails if inputs are passed as strings instead of numbers.

## Bug 5 - bug5.c
**Intended Behavior**: Calculate sum of array elements in C.
**Issue Type**: Off-by-one / Buffer over-read.
**Notes**: Loop runs up to i <= size instead of i < size, causing segmentation fault or invalid memory access.
