def divide_numbers(a, b):
    """Returns the result of a divided by b, rounded to two decimals."""
    if b == 0:
        return "Cannot divide by zero"
    result = a / b
    return round(result, 2)


def reverse_string(s):
    """Returns the reversed string, with each character's case flipped."""
    if not isinstance(s, str):
        s = str(s)     # Converts a non string into a string
    reversed_s = s[::-1]  # Bug: Might not handle non-string input properly
    flipped_case = ''.join([char.swapcase() for char in reversed_s])
    return flipped_case


def get_list_element(lst, index):
    """Returns the element at the given index in the list, or 'Not Found' if out of range."""
    if index == -1:
        return lst[-1]   # Returns the last value of the list
    elif index < -1 or index >= len(lst):  # Index less than -1 or greater than or equal to list length
        return "Not Found"  # Return 'Not Found' for out of range indices
    return lst[index]  # Return the element at the given index# Bug: Should probably raise an exception instead