from pathlib import Path

import pytest


@pytest.fixture
def test_data_path():
    """
    To be sure that we know where the test input is located
    we create a fixture which tells us the file location
    of this file.
    """
    yield Path(__file__).parent
