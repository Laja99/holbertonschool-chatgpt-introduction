#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function: factorial

    Description:
        Calculates the factorial of a given non-negative integer using recursion.
        The factorial of 0 is defined as 1. For n > 0, factorial(n) = n * factorial(n-1).

    Parameters:
        n (int): A non-negative integer whose factorial is to be calculated.

    Returns:
        int: The factorial of the given number n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Get the input number from command line arguments
f = factorial(int(sys.argv[1]))

# Print the factorial
print(f)

