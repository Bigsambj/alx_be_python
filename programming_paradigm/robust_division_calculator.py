#!/usr/bin/python3
"""
Module: robust_division_calculator
Provides a function to safely divide two numbers with proper error handling.
"""

def safe_divide(numerator, denominator):
    """
    Performs division while handling errors like division by zero and non-numeric inputs.

    Args:
        numerator: The numerator value (can be string input).
        denominator: The denominator value (can be string input).

    Returns:
        str: A message indicating the result or the error encountered.
    """
    try:
        # Attempt to convert inputs to floats
        num = float(numerator)
        den = float(denominator)

        # Perform the division
        result = num / den
        return f"The result of the division is {result}"

    except ValueError:
        return "Error: Please enter numeric values only."
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
