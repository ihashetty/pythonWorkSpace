"""Checking if the items are legit"""


def validate(ice_cream):

    """to validate icecream flavour"""
    fixed_offerings = ("vanilla", "chocolate", "straberry", "mango",
                       "vanilla choco chip", "butterscotch")

    if ice_cream.lower() in fixed_offerings:
        return True
    return False
