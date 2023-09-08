from pathlib import Path
from typing import List, Tuple, Union

from terrain_slope import calculate_slope


def read_coordinates(file_name: Union[str, Path]) -> List[Tuple[float, float]]:
    """
    Will read a file of comma separated strings and turn it
    into a list
    """
    coordinates = []
    with open(file_name, "r", encoding="utf-8") as input_file:
        for line in input_file:
            _x, _y = line.strip().split(",")
            coordinates.append((float(_x), float(_y)))
    return sorted(coordinates)


def treasure_search() -> Tuple[float, float]:
    """
    Loads a treasure map, and step by step calculates the slope
    to find the treasure (if any) and returns (x, y) of that point
    """
    treasure_map_file = "../../maps/treasure_map_1.txt"
    treasure_map = read_coordinates(treasure_map_file)
    previous_pos = None

    for current_pos in treasure_map:
        if previous_pos:
            slope = calculate_slope(previous_pos, current_pos)

            if slope >= 1.0:
                print(f"Found treasure at ({current_pos[0]}, {current_pos[1]})")
                return current_pos

        previous_pos = current_pos

    raise RuntimeError("Cannot find treasure")


def main():
    treasure_search()


if __name__ == "__main__":
    main()
