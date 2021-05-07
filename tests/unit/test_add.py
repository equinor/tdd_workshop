# 1
# Create a simple String calculator with a method signature:
# int Add(string numbers)
# The method can take up to two numbers, separated by commas, and will return their sum.
# For example “” or “1” or “1,2” as inputs.
# For an empty string it will return 0.

# def test_add():
#     string = "1,2"
#     result = add_string(string)
#     assert result == 1 + 2
# Add a little test
# Run all tests and fail # NameError: name 'add_string' is not defined
# Add items to a todo list rather than adressing them all at one


# 2
# from operators.add import add_string

# def test_add():
#     string = "1,2"
#     result = add_string(string)
#     assert result == 1 + 2

# Make a little change
# Run the tests and succeed, first time green!
# Discussion: Commit, how often?

# 3, 4, 5, 6
# from operators.add import add_string

# def test_add():
#     string = "1,2"
#     result = add_string(string)
#     assert result == 1 + 2

# Refactor to remove duplication
# Discussion: gradually generalizing the code

# 7
# from operators.add import add_string

# def test_add_standard_string():
#     string = "1,2"
#     result = add_string(string)
#     assert result == 1 + 2

# def test_add_one_number_in_the_string():
#     string = "1"
#     result = add_string(string)
#     assert result == 1 + 0

# Add a new test (passes with current function)

# 8
# from operators.add import add_string


# def test_add_standard_string():
#     string = "1,2"
#     result = add_string(string)
#     assert result == 1 + 2


# def test_add_one_number_in_the_string():
#     string = "1"
#     result = add_string(string)
#     assert result == 1 + 0


# def test_add_empty_string():
#     string = ""
#     result = add_string(string)
#     assert result == 0 + 0

# Add a new test

# 9
# from operators.add import add_string
# import pytest


# @pytest.mark.parametrize("string, expected_result", [("1,2", 1 + 2), ("1", 1), ("", 0+0)])
# def test_add_standard_string(string, expected_result):
#     result = add_string(string)
#     assert result == expected_result

# Refactor tests
# Push to testing pipeline
# Discussion:
# - Main fixtures and tools in pytest
# - Use of continuous integration
# - How to learn further (mindset DRY to identify where to improve, PR comments, books)

# 10 Allow the Add method to handle an unknown amount of numbers.
# from operators.add import add_string
# import pytest


# @pytest.mark.parametrize(
#     "string, expected_result", [("1,2", 1 + 2), ("1", 1), ("", 0 + 0), ("1,2,3", 1 + 2 + 3)]
# )
# def test_add_standard_string(string, expected_result):
#     result = add_string(string)
#     assert result == expected_result

# Add test for new requirement, green :-)

# 11
# Allow the Add method to handle new lines between numbers (instead of commas):
# The following input is ok: “1\n2,3” (will equal 6)
# The following input is NOT ok: “1,\n” (not need to prove it - just clarifying)

# from operators.add import add_string
# import pytest


# @pytest.mark.parametrize(
#     "string, expected_result", [
#         ("1,2", 1 + 2),
#         ("1", 1),
#         ("", 0 + 0),
#         ("1,2,3", 1 + 2 + 3),
#         ("1\n2,3", 1 + 2 + 3)],
# )
# def test_add_standard_string(string, expected_result):
#     result = add_string(string)
#     assert result == expected_result

# Add test for new requirement, red
# Discussion: formatting tool black

# 12, 13
# from operators.add import add_string
# import pytest


# @pytest.mark.parametrize(
#     "string, expected_result", [
#         ("1,2", 1 + 2),
#         ("1", 1),
#         ("", 0 + 0),
#         ("1,2,3", 1 + 2 + 3),
#         ("1\n2,3", 1 + 2 + 3),
#         ]
# )
# def test_add_standard_string(string, expected_result):
#     result = add_string(string)
#     assert result == expected_result

# test green
# refactor

# 14 new requirement
# Support different delimiters:
# To change a delimiter, the beginning of the string will contain a separate line that looks like this:
# “//[delimiter]\n[numbers…]” for example “//;\n1;2” should return three
#  where the default delimiter is ‘;’.
# The first line is optional.
# All existing scenarios should still be supported.

from operators.add import add_string
import pytest


@pytest.mark.parametrize(
    "string, expected_result",
    [
        ("//;\n1;2", 1 + 2),
        ("1,2", 1 + 2),
        ("1", 1),
        ("", 0 + 0),
        ("1,2,3", 1 + 2 + 3),
        ("1\n2,3", 1 + 2 + 3),
    ],
)
def test_add_standard_string(string, expected_result):
    result = add_string(string)
    assert result == expected_result


# failing test
# green test
# 15: refactor
