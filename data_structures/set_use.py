"""Set example"""


myset1 = {"Apple", 10, "Orange", "Grapes", 20.0}
myset2 = {30.0, 10, "Orange", "Apple", 40}

print("Union: ", myset1 | myset2)
print("Intersection: ", myset1 & myset2)
print("Diff: ", myset1 - myset2)
print("Symm diff: ", myset1 ^ myset2)
