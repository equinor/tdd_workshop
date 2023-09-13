from click.testing import CliRunner

from src.tdd_workshop.cli import main


def test_that_cli_fails_when_file_is_missing():
    runner = CliRunner()
    result = runner.invoke(main, ["not_a_file"])
    assert result.exit_code != 0
    assert " Path 'not_a_file' does not exist" in result.output


def test_that_cli_prints_coordinates(monkeypatch, tmp_path):
    monkeypatch.chdir(tmp_path)
    expected_coordinates_list = [
        ("2.0", "1.9"),
        ("2.5", "1.5"),
        ("3.3", "7.3"),
    ]
    with open("test_input", "w", encoding="utf-8") as fout:
        fout.write("\n".join(",".join(coords) for coords in expected_coordinates_list))
    runner = CliRunner()
    result = runner.invoke(main, ["test_input"])
    assert result.exit_code == 0
    assert (
        "coordinates: [(2.0, 1.9), (2.5, 1.5), (3.3, 7.3)]" in result.output
    )
