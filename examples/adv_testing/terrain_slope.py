import math


def calculate_slope(a: tuple[float, float], b: tuple[float, float]) -> float:
    """
    >>> calculate_slope((1.0, 0.0), (2.0, 0.0))
    0.0
    >>> calculate_slope((1.0, 0.0), (2.0, 1.0))
    1.0
    >>> calculate_slope((1.0, 0.0), (2.0, "mystring"))
    Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
        File "/Users/ANDRLI/Project/tdd/treasurehunt.py", line 35, in calculate_slope
        return (b[1] - a[1]) / (b[0] - a[0])
    TypeError: unsupported operand type(s) for -: 'str' and 'float'
    """

    # (y2 - y1) / (x2 - x1)
    return (b[1] - a[1]) / (b[0] - a[0])
