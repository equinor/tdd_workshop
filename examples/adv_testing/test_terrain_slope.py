import pytest

from terrain_slope import calculate_slope


def test_simple_slopes():
    assert pytest.approx(calculate_slope((1.0, 0.0), (2.0, 1.0))) == 1.0
    assert pytest.approx(calculate_slope((1.0, 0.0), (2.0, 0.0))) == 0.0
    assert pytest.approx(calculate_slope((1.0, 0.0), (2.0, -1.0))) == -1.0


@pytest.mark.parametrize(
    "_x1, _y1, _x2, _y2, result",
    [
        (1.0, 1.0, 2.0, 2.0, 1.0),
        (2.0, 3.0, 4.0, 4.0, 0.5),
        (1.0, 1.0, 2.0, 0.0, -1.0),
        (2.0, 4.0, 4.0, 3.0, -0.5),
    ],
)
def test_input_slopes(_x1, _y1, _x2, _y2, result):
    assert pytest.approx(calculate_slope((_x1, _y1), (_x2, _y2))) == result
