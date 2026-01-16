"""exploring tuples with indexing and other related functions"""

# Defining the Tuple
MYTUPLE = ("Apple", 10, "Orange", "Grapes", 20.0, 10)

# 1. Accessing by index (index 3 is the 4th item)
print(MYTUPLE[3])        # Output: Grapes

# 2. Accessing the last item using negative indexing
print(MYTUPLE[-1])       # Output: 10

# 3. Slicing from index 2 up to (but not including) index 4
print(MYTUPLE[2:4])      # Output: ('Orange', 'Grapes')

# 4. Slicing from the beginning up to index 4
print(MYTUPLE[:4])       # Output: ('Apple', 10, 'Orange', 'Grapes')

# 5. Slicing from index 2 to the end
print(MYTUPLE[2:])       # Output: ('Orange', 'Grapes', 20.0, 10)

# 6. Slicing with negative indices
print(MYTUPLE[-4:-1])    # Output: ('Orange', 'Grapes', 20

sensor_readings = ("2026-01-16", 22.5, "Sunny", 1013.2, 45, "North", "Active")

# to print weather condition
for x in sensor_readings:
    print(x)

print(sensor_readings[-1])
print(sensor_readings[-4:-1])
print(sensor_readings[:4])
print(sensor_readings[1:4])
