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


def calculate_slope(x1, x2, y1, y2):
    return (y2 - y1) / (x2 - x1)


def treasure_hunt(input_coordinates):
    for i, (x2, y2) in enumerate(input_coordinates[1:]):
        x1, y1 = input_coordinates[i]
        if calculate_slope(x1, x2, y1, y2) > 1:
            return x2, y2
