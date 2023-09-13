import click
from tdd_workshop.io import read_coordinates, treasure_hunt  # type: ignore


@click.command()
@click.argument("file_name", type=click.Path(exists=True))
def main(file_name: str) -> None:
    coordinates = read_coordinates(file_name)
    treasure_location = treasure_hunt(coordinates)
    print(f"Found the treasure at: {treasure_location}")
