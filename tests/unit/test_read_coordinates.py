import pytest

from tdd_workshop.io import read_coordinates, calculate_slope, treasure_hunt


def test_that_we_can_split_file_into_coordinates(test_data_path):
    """
    We read a file of test input from disk and parse it
    to make sure we get the expected result. The expected
    result in this file must be kept in sync with
    the file located on disk.
    """
    expected_coordinates_list = [
        (1, 1),
        (2.0, 1.8),
        (2.5, 2.1),
        (3, 2),
        (4.3, 7.2),
        (5.3, 6.2),
    ]

    assert read_coordinates(test_data_path / "test_input") == expected_coordinates_list


@pytest.mark.parametrize(
    "input_vals, expected_result", [[[1, 2, 1, 2], 1], [[1, 2, 1, 4], 3]]
)
def test_slope_calculator(input_vals, expected_result):
    assert calculate_slope(*input_vals) == expected_result


def test_slope_calculator_without_parameterize():
    assert calculate_slope(*[1, 2, 1, 2]) == 1
    assert calculate_slope(*[1, 2, 1, 4]) == 3



def test_that_slopes_are_calculated_correctly():
    input_list = [(1, 1), (2.0, 1.8), (2.5, 2.1), (3, 2), (4.3, 7.2), (5.3, 6.2)]
    assert treasure_hunt(input_list) == (4.3, 7.2)
