"""
This script contains functions for performing expensive operations, profiling the code for
performance optimization, and tracking the results with coverage reports.
"""
from line_profiler import profile

@profile
def expensive_op(n):
    """
    Perform a mathematical operation by multiplying n with the sum of the first 999 numbers.

    This function calculates the sum of the products of n with numbers from 0 to 999 using a formula
    to improve performance compared to a loop-based approach.

    Args:
        n (int): The multiplier to apply to the sum of numbers from 0 to 999.

    Returns:
        int: The result of the operation.
    """
    return (n * 999 * 1000) // 2

@profile
def slow_func(lst):
    """
    Apply the expensive_op function to each element in the input list and return the results.

    This function iterates over the list of numbers and calls `expensive_op` on each element,
    collecting the results in a new list.

    Args:
        lst (list): A list of integers to process.

    Returns:
        list: A list of results from calling `expensive_op` on each number.
    """
    return [expensive_op(i) for i in lst]


def main():
    """
    The main entry point of the program. It initializes a range of numbers, processes them with
    slow_func, and prints 'Done' once the processing is complete.

    This function simulates a workload by processing a range of numbers (from 0 to 999) through
    the `slow_func`. The result is not used, but the program will print "Done" when the work is
    completed.
    """
    slow_func(range(1000))
    print("Done")


if __name__ == "__main__":
    main()
