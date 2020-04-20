from unittest.mock import patch

import pytest
from pytest import raises

from molecule_parser.molecule_parser import parse_molecule

FORMULAS = {
    'H2O': {'H': 2, 'O': 1},
    'Mg(OH)2': {'Mg': 1, 'O': 2, 'H': 2},
    'K4[ON(SO3)2]2': {'K': 4, 'O': 14, 'N': 2, 'S': 4},
    'Fe(NO3)2': {'Fe': 1, 'N': 2, 'O': 6}
}


def test_parse_molecule_result():
    for formula, result in FORMULAS.items():
        assert parse_molecule(formula) == result


@patch('molecule_parser.molecule_parser.str_to_dict')
@patch('molecule_parser.molecule_parser.is_contain_brackets')
@patch('molecule_parser.molecule_parser.recurse')
def test_parse_molecule_without_bracket(mock_recurse, mock_is_contain_brackets, mock_str_to_dict):
    mock_is_contain_brackets.return_value = False
    parse_molecule('H2O')
    mock_str_to_dict.assert_called_once()
    mock_recurse.assert_not_called()


@pytest.mark.parametrize(("formula", "exception"),
                         [('Mg(OH2', ValueError),
                          (12, TypeError)])
def test_parse_molecule_raises_exception(formula, exception):
    with raises(exception):
        parse_molecule(formula)
