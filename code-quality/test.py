import pytest
from main import expensive_op, slow_func

def test_expensive_op():
    assert expensive_op(5) == 24975000  # Example expected result.

def test_slow_func():
    result = slow_func([1, 2, 3])
    assert len(result) == 3  # Ensure that the result length is correct.
