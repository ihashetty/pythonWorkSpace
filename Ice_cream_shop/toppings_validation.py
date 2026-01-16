"""Checking if the items are legit"""


def validate(topping_list):

    """validated the servinging"""
    toppings = {"choco chips", "sprinklers", "fruit"}
    if not topping_list:
        return True
    for x in topping_list:

        if x.lower() not in toppings:
            return False
    return True
