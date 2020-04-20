import pytest

from molecule_parser.tools import compute_multiplier


@pytest.mark.parametrize(("formula", "index", "expected"),
                         [('OH)2', 2, (2, 3)),
                          ('SO3)2)2', 3, (2, 4)),
                          ('ON(SO3)2)2', 8, (2, 9))])
def test_compute_multiplier(formula, index, expected):
    assert compute_multiplier(formula, index) == expected
