"""This is employee class"""


class Employee:

    """Class to initialise"""
    def __init__(self, id, name, age, salary):
        self.id = id
        self.name = name
        self.age = age
        self.salary = salary

    def display(self):

        """To display details of the employee"""
        print(f"Employee name is {self.name} of age"
              f"{self.age} and having salary {self.salary}")


obj1 = Employee(100, "iha", 20, 12345678901223445567889)
obj1.display()
obj2 = Employee(101, "Nethra", 20, 1234567876543)
obj2.display()
obj3 = Employee(102, "Nitya", 20, 191991919)
obj3.display()

emps = {obj1.id: obj1, obj2.id: obj2, obj3.id: obj3}
emp5 = Employee(101, "Smith", 25, 45000)
flag = False
for emp in emps:
    if (emps[emp].id == emp5.id):
        print("Already Exists")
        flag = True
        break
if not flag:
    emps.update({"emp5": emp5})

for emp in emps:
    emps[emp].display()
