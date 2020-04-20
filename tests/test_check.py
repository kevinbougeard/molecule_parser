import pytest

from molecule_parser.check import is_contain_brackets, is_formatting


@pytest.mark.parametrize(("formula", "expected"),
                         [('(HO)2O', True),
                          ('H2O', False)])
def test_is_contain_brackets_return(formula, expected):
    assert is_contain_brackets(formula) == expected


@pytest.mark.parametrize(("formula", "expected"),
                         [("H2O", True),
                          ("H2(O", False),
                          ("H2(O)2", True),
                          ("H2{{O}}", True),
                          ("H2{{O}", False),
                          ("K(H{ON}2)3", True),
                          ("K(H{ON}2)3]", False)])
def test_is_formatting_return(formula, expected):
    assert is_formatting(formula) is expected
