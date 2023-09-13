from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pathlib import Path
    from typing import Union, List, Tuple


def read_coordinates(file_name: Union[str, Path]) -> List[Tuple[float, float]]:
    """
    Read a file of comma separated strings and turn it into a list of floats.
    """
    coordinates = []
    with open(file_name, "r", encoding="utf-8") as input_file:
        for line in input_file:
            x, y = line.strip().split(",")
            coordinates.append((float(x), float(y)))
    return coordinates

def calculate_slope_along_coordinates(coordinates: List[Tuple[float, float]]) -> List[float]:
    """Given list of coordinates, calculate the slope."""
    slopes = []
    for i in range(len(coordinates)-1):
        p1 = coordinates[i]
        p2 = coordinates[i+1]
        slopes.append(slope(p1, p2))

    return slopes        

def find_coordinate_based_on_incline_treshold(coordinates, treshold):
    """Given a list of coordinates, find the coordinate directly 
    AFTER the FIRST instance of an incline ABOVE treshold.
    
    Example:
    Slope between p1 and p2 is 1.5, the treshold is 1, then return p2.
    """

    for i in range(len(coordinates)-1):
        p1 = coordinates[i]
        p2 = coordinates[i+1]
        if slope(p1, p2) > treshold:
            return p2
    


def slope(p1, p2):
    """Calculate slope from p1 to p2."""
    x1, y1 = p1
    x2, y2 = p2

    _slope = (y2-y1)/(x2-x1)
    _slope = round(_slope, 2)
    return _slope