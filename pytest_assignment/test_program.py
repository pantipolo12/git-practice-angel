import pytest
from program import divide_numbers, reverse_string, get_list_element

# Test for divide_numbersx
def test_divide_numbers_normal():
    assert divide_numbers(10, 2) == 5.0

def test_divide_numbers_with_zero():
    assert divide_numbers(10, 0) == "Cannot divide by zero"

def test_divide_numbers_with_negative():
    assert divide_numbers(-10, 2) == -5.0

# Test for reverse_strings
def test_reverse_string():
    assert reverse_string("hello world") == "DLROW OLLEH"

def test_reverse_string_non_string_input():
    assert reverse_string(123) == "321"

def test_reverse_string_empty_string():
    assert reverse_string("") == ""

# Test for get_list_element
def test_get_list_element():
    assert get_list_element([1, 2, 3], 1) == 2

def test_get_list_element_out_of_range():
    assert get_list_element([1, 2, 3], 4) == "Not Found"

def test_get_list_element_negative_index():
    assert get_list_element([1, 2, 3], -1) == 3