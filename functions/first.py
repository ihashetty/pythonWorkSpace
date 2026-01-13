"""Python functions"""


def hello(name):
    """This is Hello"""
    print("Hello", name)


def greet_people(name, title):
    """This is to greet"""
    print("Hello", title, name)


def sum_val(a, b):
    """this is for sum"""
    return a+b


hello("Iha")
greet_people("iha", "miss")

RESULT = sum_val(10, 20)
print(RESULT)


