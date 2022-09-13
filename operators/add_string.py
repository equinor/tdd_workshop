from .string_to_number import string_to_numbers

"""
This contains the add_string method

"""

def add_string(txt: str) -> int:
    """Return the sum of numbers in the incoming string"""

    # verify input is a string
    if not isinstance(txt, str):
        raise TypeError("txt must be a string")
    
    numbers = string_to_numbers(txt)

    return sum(numbers)


