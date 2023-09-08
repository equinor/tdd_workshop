from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pathlib import Path
    from typing import Union, List, Tuple


def read_coordinates(file_name: Union[str, Path]) -> List[Tuple[float, float]]:
    """
    Will read a file of comma separated strings and turn it
    into a list
    """
    coordinates = []
    with open(file_name, "r", encoding="utf-8") as input_file:
        for line in input_file:
            x, y = line.strip().split(",")
            coordinates.append((float(x), float(y)))
    return coordinates


def calculate_diff_coordinates(coordinates):
    diff_coordinates = []
    for coordinate_number, (x, y) in enumerate(coordinates):
        if coordinate_number == 0:
            (x0, y0) = (x, y)
        else:
            diff_coordinates.append((float(round(x - x0, 4)), float(round(y - y0, 4))))
            (x0, y0) = (x, y)

    return diff_coordinates


def calculate_slopes(diff_coordinates):
    slopes_list = []
    for diff_coordinate_number, (x, y) in enumerate(diff_coordinates):
        slopes_list.append(y / x)

    return slopes_list


def get_slope_index_based_on_threshold(slopes_list, threshold):
    for slope_index, slope in enumerate(slopes_list):
        if slope >= threshold:
            return slope_index


def treasure_coordinate(input_file, threshold):
    coordinates = read_coordinates(input_file)
    diff_coordinates = calculate_diff_coordinates(coordinates)
    slopes_list = calculate_slopes(diff_coordinates)
    slope_index = get_slope_index_based_on_threshold(slopes_list, threshold)

    return coordinates[slope_index + 1]
