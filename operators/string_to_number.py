def string_to_int(string_input):
    return int(string_input)


def string_to_numbers(txt: str) -> tuple:
    """Convert the txt to a tuple of ints"""

    numbers = []
    for elem in txt.split(","):
        try:
            numbers.append(int(elem))
        except ValueError:
            raise TypeError("non-valid input: %s", elem)

    return tuple(numbers)
