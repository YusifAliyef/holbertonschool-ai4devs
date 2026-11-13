## bug1.py
- Original Issue: Off-by-one
- Fix Applied: Adjusted slice to items[len(items) - n:]
- Test Results: All 3 test cases passed

## bug2.js
- Original Issue: Loop condition i <= numbers.length read past the end of the array, adding undefined and returning NaN
- Fix Applied: Changed loop condition to i < numbers.length
- Test Results: All 3 test cases passed

## bug3.java
- Original Issue: Strings compared with == (reference comparison) instead of content
- Fix Applied: Replaced == with .equals()
- Test Results: All 3 test cases passed

## bug4.py
- Original Issue: Mutable default argument tags=[] shared between calls
- Fix Applied: Used tags=None and created a new list inside the function
- Test Results: All 2 test cases passed

## bug5.js
- Original Issue: var is function-scoped so all callbacks shared the same i and printed 3
- Fix Applied: Replaced var with let so each iteration has its own i
- Test Results: All 3 outputs correct (0, 1, 2)
