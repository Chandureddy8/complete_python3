class NegativeNumbersError(Exception):
    """One or more inputs are negative"""
    pass

def add_positive_numbers(a, b):
    try:
        if a <= 0 or b <= 0:
            raise NegativeNumbersError
    except NegativeNumbersError:
        return "Shame on you, not valid!"

print(add_positive_numbers(-5, -2))