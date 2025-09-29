# arithmetic_operations.py

def perform_operation(num1, num2, operation):
    """
    Perform a basic arithmetic operation.

    Parameters
    ----------
    num1 : float
        First number.
    num2 : float
        Second number.
    operation : str
        One of: 'add', 'subtract', 'multiply', 'divide'.

    Returns
    -------
    float or str
        The numeric result of the operation,
        or an error message if invalid operation or division by zero.
    """
    operation = operation.strip().lower()

    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    else:
        return f"Error: Unsupported operation '{operation}'"
