from unittest.mock import patch

import pytest

from molecule_parser.recurse import recurse


@pytest.mark.parametrize(("formula", "expected"),
                         [('H2O', ({'H': 2, 'O': 1})),
                          ('O', ({'O': 1}))])
def test_str_to_dict_return(formula, expected):
    assert recurse(formula) == (expected, len(formula))


@patch('molecule_parser.recurse.compute_multiplier')
@patch('molecule_parser.recurse.str_to_dict')
def test_str_to_dict_calls_with_one_bracket(mock_str_to_dict, mock_compute_multiplier):
    mock_str_to_dict.return_value = {'O': 1, 'H': 1}
    mock_compute_multiplier.return_value = (2, 3)
    recurse('Mg(OH)2')
    mock_str_to_dict.assert_called()
    mock_compute_multiplier.assert_called_once()


@patch('molecule_parser.recurse.compute_multiplier')
@patch('molecule_parser.recurse.str_to_dict')
def test_str_to_dict_calls_with_no_bracket(mock_str_to_dict, mock_compute_multiplier):
    recurse('H20')
    mock_str_to_dict.assert_called_once()
    mock_compute_multiplier.assert_not_called()
