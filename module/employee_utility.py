"""This is to calculate employee total salary with bonus and leave cuts"""

from salary_calc import salary_calc

position = input("Enter your designation").lower()
base_sal = float(input("Enter the base salary"))
print(salary_calc(position, base_sal))
