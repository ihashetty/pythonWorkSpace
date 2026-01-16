"""To try and explore dictionary and diff funstions associated with it"""


# Define the Dictionary
MYFRIENDS = {"Sandy": 25, "John": 20, "Jane": 22}

# Accessing components
print(MYFRIENDS.items())   # View all pairs
print(MYFRIENDS.keys())    # View all names
print(MYFRIENDS.values())  # View all ages
print(MYFRIENDS["Sandy"])  # Get Sandy's age -> 25

# Updating values
MYFRIENDS["Sandy"] = 30    # Change age to 30
print(MYFRIENDS.items())

MYFRIENDS.update({"Sandy": 40})  # Update method
print(MYFRIENDS.items())

# Removing items
MYFRIENDS.pop("Sandy")     # Removes Sandy specifically
print(MYFRIENDS.items())

MYFRIENDS.popitem()        # Removes the last inserted item
print(MYFRIENDS.items())

del MYFRIENDS["John"]      # Another way to delete a specific key
print(MYFRIENDS.items())
