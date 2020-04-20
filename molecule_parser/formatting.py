import re


def str_to_dict(formula: str) -> dict:
    """
    Convert a string chemical formula to dict occurrences of each atom

    :param formula: chemical formula
    :type formula: string
    :return: atom on key and number of occurrences in value
    :rtype: dictionary
    """
    tuples = re.findall(r'([A-Z][a-z]*)(\d*)', formula)
    res = {}
    for element, number in tuples:
        res[element] = (res[element] + int(number or 1)) if element in res else int(number or 1)
    return res
