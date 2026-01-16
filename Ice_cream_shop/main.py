""""You have been hired to build a management system for
a new boutique ice cream shop, "Scoops & Scripts."
 The shop owner needs a robust
program that ensures the menu remains permanent, prices are easily
searchable, and
order history is tracked accurately.

Project Requirements
Your task is to implement a system using Python that handles different types of
 data with specific constraints:

Fixed Offerings: The basic flavors (Vanilla, Chocolate, Strawberry) are the
shop's signature and should never be accidentally changed or deleted during the
program's execution.

Pricing Lookup: Each flavor has a specific price.
The system must quickly find the cost
 of a flavor to calculate a customer's bill.

Strict Serving Rules: To prevent inventory errors,
the shop only allows two types of serving: Cone or Cup. This rule is set in
stone and must be immutable.

Customization: Customers can choose multiple toppings. These toppings should
be unique (you can't have "nuts" twice), and the order doesn't matter.

Transaction Tracking: The system must maintain a running
history of every successful sale made throughout the day so that the
 manager can review them at closing."""


from bill_calc import bill_amt
import icecream_validation
import serving_validation
import toppings_validation

history = []


def place_order():

    """This function will validate the input and place order"""
    ice_cream = ''
    servings = ''
    topping = []
    while True:
        ice_cream = input('Choose ice cream of your choice')
        if icecream_validation.validate(ice_cream) is False:
            print("This ice cream is not available, pls choose from the menu")
        else:
            break

    while True:
        servings = input('choose a serving, cup or cone')
        if serving_validation.validate(servings) is False:
            print("This serving is not available, pls choose from the menu")
        else:
            break

    while True:
        h = []
        print("Enter toppings one per line. Type 0 to finish.")
        while True:
            raw = input("Choose topping (or 0 to finish): ").strip()
            if raw == "0":
                break
            if not raw:
                continue  # skip empty lines
            h.append(raw)

        toppings = []
        seen = set()
        for item in h:
            for t in item.split(","):
                t = t.strip().lower()
                if t and t not in seen:
                    seen.add(t)
                    toppings.append(t)

        if toppings_validation.validate(toppings) is False:
            print("These toppings are not available."
                  " Please choose from the menu.")
        else:
            break

    total_amt = bill_amt(ice_cream, servings, topping)
    print("Total amount is:", total_amt)

    history.append(total_amt)

    print(history)


if __name__ == "__main__":
    place_order()
