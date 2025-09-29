"""
arithmetic_operations.py

Provides perform_operation(num1: float, num2: float, operation: str) -> float | str

Accepted operations (case-insensitive):
 - 'add'       -> returns num1 + num2
 - 'subtract'  -> returns num1 - num2
 - 'multiply'  -> returns num1 * num2
 - 'divide'    -> returns num1 / num2, or a recognizable error message if division by zero

For error cases (division by zero or invalid operation) the function returns a string
message that the provided main.py can print directly.
"""

from typing import Union

def perform_operation(num1: float, num2: float, operation: str) -> Union[float, str]:
    """
    Perform a basic arithmetic operation.

    Parameters
    ----------
    num1 : float
        The first number.
    num2 : float
        The second number.
    operation : str
        One of: 'add', 'subtract', 'multiply', 'divide' (case-insensitive).

    Returns
    -------
    float or str
        The numeric result for successful operations, or a string error message:
        - "Error: Division by zero" when attempting to divide by zero.
        - "Error: Invalid operation" for unsupported operation strings.
    """
    if not isinstance(operation, str):
        return "Error: Invalid operation"

    op = operation.strip().lower()

    if op == 'add':
        return num1 + num2
    elif op == 'subtract':
        return num1 - num2
    elif op == 'multiply':
        return num1 * num2
    elif op == 'divide':
        # handle division by zero (use a tiny epsilon to be robust with floats)
        if abs(num2) < 1e-12:
            return "Error: Division by zero"
        return num1 / num2
    else:
        return "Error: Invalid operation"
