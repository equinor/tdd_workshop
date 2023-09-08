from unittest.mock import patch

import pytest

import treasurehunt


@patch("treasurehunt.read_coordinates")
def test_another_treasure(mock_read_coordinates):
    mock_read_coordinates.return_value = [
        (0.0, 0.0),
        (1.0, 0.0),
        (2.0, 0.5),
        (3.0, 1.0),
        (4.0, 4.0),
    ]

    point = treasurehunt.treasure_search()
    assert pytest.approx(point) == (4.0, 4.0)
