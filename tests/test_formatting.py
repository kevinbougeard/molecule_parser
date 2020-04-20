import pytest

from molecule_parser.formatting import str_to_dict


@pytest.mark.parametrize(("formula", "expected"),
                         [('H2O', {'H': 2, 'O': 1}),
                          ('O', {'O': 1})])
def test_str_to_dict(formula, expected):
    assert str_to_dict(formula) == expected
