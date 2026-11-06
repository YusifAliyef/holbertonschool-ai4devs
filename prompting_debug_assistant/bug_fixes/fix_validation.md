## Bug 1 - bug1_fixed.py
- **Test Case**: Retrieve last 3 items from a list of 5 elements.
- **Input**: `items = [1, 2, 3, 4, 5], n = 3`
- **Expected Output**: `[3, 4, 5]`
- **Actual Output**: `[3, 4, 5]`
- **Validation Status**: PASS ✅
- **Explanation**: Negative slicing `items[-n:]` correctly handles boundary conditions without index out of bounds exceptions.

## Bug 2 - bug2_fixed.js
- **Test Case**: Calculate total cart value with multiple item prices.
- **Input**: `cartItems = [{price: 10}, {price: 20}]`
- **Expected Output**: `30`
- **Actual Output**: `30`
- **Validation Status**: PASS ✅
- **Explanation**: Loop condition corrected from `<=` to `<` prevents accessing undefined property at index equal to length.

## Bug 3 - bug3_fixed.py
- **Test Case**: Parse a valid comma-separated user data string.
- **Input**: `data_string = "Yusif, 21"`
- **Expected Output**: `{"username": "Yusif", "age": 21}`
- **Actual Output**: `{"username": "Yusif", "age": 21}`
- **Validation Status**: PASS ✅
- **Explanation**: Length and format validations prevent IndexError when parsing malformed strings.

## Bug 4 - bug4_fixed.js
- **Test Case**: Subtract discount from base price with numeric conversion.
- **Input**: `price = 100, discount = 20`
- **Expected Output**: `80`
- **Actual Output**: `80`
- **Validation Status**: PASS ✅
- **Explanation**: Explicit parsing using `parseFloat()` prevents string concatenation/type mismatch issues.

## Bug 5 - bug5_fixed.c
- **Test Case**: Sum all elements of an integer array in C.
- **Input**: `arr = {1, 2, 3, 4, 5}, size = 5`
- **Expected Output**: `15`
- **Actual Output**: `15`
- **Validation Status**: PASS ✅
- **Explanation**: Loop condition changed from `i <= size` to `i < size` successfully eliminates buffer over-read and segmentation faults.
