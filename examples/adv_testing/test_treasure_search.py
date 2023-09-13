from pathlib import Path
from typing import Union

import pytest

import treasurehunt


def test_find_treasure(monkeypatch):
    def mock_read_coordinates(file_name: Union[str, Path]):
        return [(0.0, 0.0), (1.0, 0.0), (2.0, 2.0)]

    monkeypatch.setattr(treasurehunt, "read_coordinates", mock_read_coordinates)
    point = treasurehunt.treasure_search()
    assert pytest.approx(point) == (2.0, 2.0)


def test_find_treasure_raises_on_flat_ground(monkeypatch):
    def mock_read_coordinates(file_name: Union[str, Path]):
        return [(0.0, 0.0), (1.0, 0.0), (2.0, 0.0)]

    monkeypatch.setattr(treasurehunt, "read_coordinates", mock_read_coordinates)

    with pytest.raises(RuntimeError, match="Cannot find treasure"):
        treasurehunt.treasure_search()
