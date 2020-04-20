import re


def compute_multiplier(formula: str, index: int) -> tuple:
    """
    Compute multiplier for each atom in formula

    :param formula: chemical formula
    :type formula: string
    :param index: place of cursor in complete formula string
    :type index: integer
    :return: tuple composed of multiplier and index updated
    :rtype: tuple
    """
    multiplier = 1
    match = re.match(r'\d+', formula[index + 1:])
    if match:
        multiplier = int(match.group(0))
        index += len(match.group(0))
    return multiplier, index
