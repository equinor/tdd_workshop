from tdd_workshop.io import read_coordinates, calculate_slope_along_coordinates, slope, find_coordinate_based_on_incline_treshold
from typing import Union, List, Tuple
import pytest


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

@pytest.mark.parametrize("p1, p2, expected_slope", [
    ((1,1), (2.0, 1.8), 0.8),
    ((2.0, 1.8), (2.5, 2.1), 0.6),
    ((2.5, 2.1), (3, 2), -0.2)
    ])
def test_slope(p1, p2, expected_slope):
    """Test the slope method."""
    assert slope(p1, p2) == expected_slope

def test_calculate_slope_along_coordinates():
    """Test the calculate_slope_along_coordinates method."""
    datain = [(1, 1), (2.0, 1.8), (2.5, 2.1), (3, 2), (4.3, 7.2), (5.3, 6.2)]
    expected = [0.8, 0.6, -0.2, 4.0, -1.0]  # be wary of rounding of these numbers
    assert calculate_slope_along_coordinates(datain) == expected

def test_find_coordinates_based_on_incline():
    """Test the bla bla method."""
    datain = [(1, 1), (2.0, 1.8), (2.5, 2.1), (3, 2), (4.3, 7.2), (5.3, 6.2)]
    treshold = 1
    expected = (4.3, 7.2)

    assert find_coordinate_based_on_incline_treshold(datain, treshold) == expected