
"""Student marks docstring"""
marks = int(input("enter marks"))

if 90 <= marks <= 100:
    print("Grade A")
elif 70 <= marks < 90:
    print("Grade B")
elif 50 <= marks < 70:
    print("Grade C")
elif 30 <= marks < 50:
    print("Grade D")
else:
    print("Fail")
