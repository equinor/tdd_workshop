from tdd_workshop.io import read_coordinates


def test_that_we_can_split_file_into_coordinates(test_data_path):
    """
    We read a file of test input from disk and parse it
    to make sure we get the expected result. The expected
    result in this file must be kept in sync with
    the file located on disk.
    """
    expected_coordinates_list = [
        (float("1"), float("1")),
        (float("2.0"), float("1.8")),
        (float("2.5"), float("2.1")),
        (float("3"), float("2")),
        (float("4.3"), float("7.2")),
        (float("5.3"), float("6.2")),
    ]

    assert read_coordinates(test_data_path / "test_input") == expected_coordinates_list
