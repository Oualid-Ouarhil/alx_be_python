def safe_divide(numerator, denominator):
    try:
        numb1 = float(numerator)
        deno1 = float(denominator)

        result = numb1 / deno1
        return f"The result of the division is {result:.1f}"
    
    except ZeroDivisionError:
        return 'Error: Cannot divide by zero.'
    except ValueError:
        return 'Error: Please enter numeric values only.'