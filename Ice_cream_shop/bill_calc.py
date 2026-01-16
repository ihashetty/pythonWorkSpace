"""Bill calculations for the ice cream order"""


def bill_amt(flavour, serving, toppings):

    """calculate billing total"""
    pricing_icecream = {"vanilla": 60, "chocolate": 60, "straberry": 65,
                        "mango": 100,
                        "vanilla choco chip": 75, "butterscoth": 80}
    pricing_serving = {"cone": 10, "cup": 20}
    pricing_toppings = {"choco chips": 5, "sprinkels": 5, "fruits": 10}
    bill = 0
    if flavour.lower() in pricing_icecream:
        bill += pricing_icecream[flavour]

    if serving.lower() in pricing_serving:
        bill += pricing_serving[serving]

    if not toppings:
        return bill

    for x in toppings:
        if x.lower() in pricing_toppings:
            bill += pricing_toppings[x]

    return bill
