# Fixes Documentation

### Function: divide_numbers(a, b)
#### Bug:
- No handling for division by zero 

#### How it was identified:
- When running tests for division, particularly for divide_numbers(10, 0), the test failed due to an unhandled division by zero error.

#### Fix Applied:
- Added a condition to check if b == 0. If that condition is true, then it should return "Cannot divide by zero"


      def divide_numbers(a, b):
    """Returns the result of a divided by b, rounded to two decimals."""
    if b == 0:
        return "Cannot divide by zero"
    result = a / b
    return round(result, 2)

### Function: reversed_string(s)
#### Bug:
- The function originally did not handle non-string inputs properly. It would raise an error if an integer (or any non-string type) was passed in.

#### How it was identified:
- The test test_reverse_string_non_string_input failed when passing an integer to the function (e.g., reverse_string(123)), which caused a TypeError because the function expected only strings.
#### Fix Applied:
- Modified the function to check and convert non-string inputs (like integers) to strings before performing the reversal and case-flipping.
        
         
        def reverse_string(s):
    """Returns the reversed string, with each character's case flipped."""
    if not isinstance(s, str):
        s = str(s)     # Converts a non string into a string
    reversed_s = s[::-1]  # Bug: Might not handle non-string input properly
    flipped_case = ''.join([char.swapcase() for char in reversed_s])
    return flipped_case

### Function: get_list_element(lst, index)
#### Bug:
- The original function incorrectly handled out-of-range indices. 
- It didn’t handle negative indices well (-1 should return the last element).
- The function incorrectly returned "Not found" for any out-of-range indices, including when the index was -1 (last element), which was a logical error.
#### How it was identified:
- During tests, accessing valid negative indices like -1 did not return the last element. 
- Also, providing out-of-range indices returned "Not found" even for negative indices where valid elements could exist.
### Fix Applied:
Adjusted the logic, by setting the contidions: 
- If the index is -1, the function returns the last element in the list.
- If the index is less than -1 or greater than or equal to the length of the list, the function now returns "Not Found".



    def get_list_element(lst, index):
    """Returns the element at the given index in the list, or 'Not Found' if out of range."""
    if index == -1:
        return lst[-1]   # Returns the last value of the list
    elif index < -1 or index >= len(lst):  # Index less than -1 or greater than or equal to list length
        return "Not Found"  # Return 'Not Found' for out of range indices
    return lst[index