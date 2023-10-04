import click

from tdd_workshop.io import read_coordinates


@click.command()
@click.argument("file_name", type=click.Path(exists=True))
def main(file_name: str) -> None:
    coordinates = read_coordinates(file_name)
    print(f"Read file: {file_name}, coordinates: {coordinates}")
