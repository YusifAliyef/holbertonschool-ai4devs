# Bug Descriptions

## bug1.py
- **Intended Behavior**: Return the last n items in a list.
- **Current Issue**: Off-by-one error due to incorrect slicing (returns n+1 items).

## bug2.js
- **Intended Behavior**: Return the average of an array of numbers.
- **Current Issue**: The loop condition `i <= numbers.length` reads past the end of the array, adds `undefined` and the result becomes `NaN`.

## bug3.java
- **Intended Behavior**: Return true if a word is a palindrome (reads the same in both directions).
- **Current Issue**: Strings are compared with `==` (reference comparison) instead of `.equals()`, so the method returns false for real palindromes.

## bug4.py
- **Intended Behavior**: Each call to `add_tag` without a list returns a new list that contains only the given tag.
- **Current Issue**: Mutable default argument (`tags=[]`) is shared between calls, so tags accumulate across calls.

## bug5.js
- **Intended Behavior**: Print 0, 1, 2 with a 100 ms delay between them.
- **Current Issue**: `var` is function-scoped, so all callbacks share the same `i` and print `3` three times.
