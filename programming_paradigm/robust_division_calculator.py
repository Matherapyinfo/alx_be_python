def safe_divide(numerator, denominator):
    """
    Safely divides two numbers with error handling
    
    Args:
        numerator: Number to be divided (str or numeric)
        denominator: Number to divide by (str or numeric)
    
    Returns:
        str: Result message or error description
    """
    try:
        # Convert inputs to floats
        num = float(numerator)
        den = float(denominator)
    except ValueError:
        return "Error: Please enter numeric values only."
    
    try:
        result = num / den
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    
    return f"The result of the division is {result}"
