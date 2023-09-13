import click
from tdd_workshop.io import read_coordinates, find_coordinate_based_on_incline_treshold  # type: ignore


@click.command()
@click.argument("file_name", type=click.Path(exists=True))
@click.argument("treshold", default=1.0, type=float)
def main(file_name: str, treshold: float) -> None:
    coordinates = read_coordinates(file_name)
    found_coordinate = find_coordinate_based_on_incline_treshold(coordinates, treshold)
    click.clear()
    # click.echo(f"Read file: {file_name}, coordinates: {coordinates}")
    click.echo(f"\n\n\n\n 🚩 Treasure! 💰🎉✨👉 {found_coordinate}\n\n\n\n")
