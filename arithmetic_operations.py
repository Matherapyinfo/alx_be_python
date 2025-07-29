def perform_operation(num1: float, num2: float, operation: str):
     """
    Performs basic arithmetic operations on two numbers.

    Parameters:
        num1 (float): First number
        num2 (float): Second number
        operation (str): Operation type - 'add', 'subtract', 'multiply', 'divide'

    Returns:
        float: Result of arithmetic operation
        str: Error message in case of division by zero
    """
     # Convert operation to lowercase for case-insensitive matching
    operation = operation.lower()

    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero is not allowed"
        return num1 / num2
    else:
        return "Error: Invalid operation. Please choose add, subtract, multiply, or divide."


