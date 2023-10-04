from pathlib import Path
from typing import List, Tuple, Union


def read_coordinates(file_name: Union[str, Path]) -> List[Tuple[str, str]]:
    """
    Will read a file of comma separated strings and turn it
    into a list
    """
    coordinates = []
    with open(file_name, "r", encoding="utf-8") as input_file:
        for line in input_file:
            x, y = line.strip().split(",")
            coordinates.append((x, y))
    return coordinates
