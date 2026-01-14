"""This is a trial on try except and finally"""

try:
    num = int(input("Enter num:"))
    print(10 / num)
    print("hello")
except ZeroDivisionError:
    print("cannot divide by zero")
except ValueError:
    print("Invalid Input")
finally:
    print("Execution done")
