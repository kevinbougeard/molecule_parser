from collections import Counter


def is_formatting(formula: str) -> bool:
    """
    Verify number of opened and closed brackets

    :param formula: chemical formula
    :type formula: str
    :return: True if number of opened brackets equal number of closed
    :rtype: bool
    """
    c = Counter(formula)
    return c["("] == c[")"] and c["["] == c["]"] and c["{"] == c["}"]


def is_contain_brackets(formula: str) -> bool:
    """
    Verify if formula contains brackets or not

    :param formula: chemical formula
    :type formula: str
    :return: True if formula contains brackets and False else
    :rtype: bool
    """
    if [i for i in "([{)]}" if i in formula]:
        return True
    return False
