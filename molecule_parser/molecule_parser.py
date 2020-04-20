from molecule_parser.check import is_contain_brackets, is_formatting
from molecule_parser.formatting import str_to_dict
from molecule_parser.recurse import recurse


def parse_molecule(formula: str) -> dict:
    """
    Parse the formula and return a dict with occurrences of each atom.

    :param formula: chemical formula
    :type formula: string
    :return: number of atoms of each element contained in the molecule
    :rtype: dictionary
    """
    if not isinstance(formula, str):
        raise TypeError(f"{formula} is not a string")

    if not is_contain_brackets(formula):
        return str_to_dict(formula)

    if not is_formatting(formula):
        raise ValueError("Number of closed brackets not equal to opened brackets")

    return recurse(formula)[0]
