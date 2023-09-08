from hypothesis import given, reproduce_failure
from hypothesis import strategies as st

from treasurehunt import calculate_slope


@given(
    st.floats(min_value=0.0, max_value=10.0),
    st.floats(min_value=0.0, max_value=10.0),
    st.floats(min_value=0.0, max_value=10.0),
    st.floats(min_value=0.0, max_value=10.0),
)
def test_that_calculate_slope_does_not_raise(_x1, _y1, _x2, _y2):
    calculate_slope((_x1, _y1), (_x2, _y2))
