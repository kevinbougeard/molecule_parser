from collections import Counter

from molecule_parser.formatting import str_to_dict
from molecule_parser.tools import compute_multiplier


def recurse(formula: str):
    """
    Recursive method to parse a chemical formula with brackets
    Compute each sub molecule in brackets to fuse all in one and return dict

    :param formula: chemical formula
    :type formula: string
    :return: dict with atom/occurrences and place of current element into the formula
    :rtype: tuple
    """

    current_molecule = {}
    elements = ""
    index = 0

    while index < len(formula):
        current_character = formula[index]

        if current_character in "({[":
            bracket_molecule, formula_index = recurse(formula[index + 1:])
            current_molecule = dict(Counter(current_molecule) + Counter(bracket_molecule))
            index += formula_index + 1

        elif current_character in ")}]":
            multiplier, index = compute_multiplier(formula, index)
            bracket_molecule = str_to_dict(elements)
            fusion = Counter(current_molecule) + Counter(bracket_molecule)
            return {element: fusion.get(element) * multiplier for element in fusion.keys()}, index

        elements = f"{elements}{current_character}"
        index += 1

    atom_occurrences = dict(Counter(current_molecule) + Counter(str_to_dict(elements)))

    return atom_occurrences, index
