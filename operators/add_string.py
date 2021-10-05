"""
String calculation:
The method can take two numbers, separated by commas, and will return their sum.
For example "1,2" would return 3, "2,2" would return 4.
"""


def string_add(numbers: str):
    number_list = numbers.split(",")
    if len(number_list) != 2:
        raise ValueError(
            "string_add requires a string with exactly two values (comma separated)"
        )
    return float(number_list[0]) + float(number_list[1])
