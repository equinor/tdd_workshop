python treasurehunt.py
python -m doctest -v terrain_slope.py
pytest -n auto -svv test_terrain_slope.py
pytest -n auto -svv test_treasure_search.py
pytest -n auto -svv test_hypothesis_slope.py
