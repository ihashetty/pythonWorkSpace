"""This is a program exploring lists and slicing """


numbers = [1, 2, 3, 4]
numbers.append(5)
print(numbers)

MYLIST = [10, "apple", 12, 13, 14]
print("--------")
print(MYLIST)
print(MYLIST[1:2])
print(MYLIST[1:3])
print(MYLIST[:2])
print(MYLIST[2:])


ITEMS = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
if "apple" in ITEMS:
    print("Yes, 'apple' is in the fruits list")
elif "banana" in ITEMS:
    print("Yes, 'banana' is in the fruits list")
else:
    print("fruit not found")
