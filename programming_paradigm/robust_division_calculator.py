def safe_divide(numerator, denominator):
    """
    Safely divide two numbers with robust error handling.
    
    Args:
        numerator: The dividend (can be string or numeric)
        denominator: The divisor (can be string or numeric)
    
    Returns:
        str: Result message or error message
    """
    try:
        # Try to convert inputs to floats
        num = float(numerator)
        den = float(denominator)
        
        # Check for division by zero before performing division
        if den == 0:
            return "Error: Cannot divide by zero."
        
        # Perform the division
        result = num / den
        return f"The result of the division is {result}"
        
    except ValueError:
        # Handle non-numeric inputs (conversion to float failed)
        return "Error: Please enter numeric values only."
