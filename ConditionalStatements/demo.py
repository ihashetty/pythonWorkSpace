"""This is demo code"""


def eve_odd(input1):

    """To check if num is even or odd"""
    if input1 % 2 == 0:
        print("num is even")
    else:
        print("num is odd")


num = input("Enter the number : ")
eve_odd(int(num))
