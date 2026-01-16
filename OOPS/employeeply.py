"""employeeply"""


class Employee:

    """employee class"""
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_details(self):

        """getting details of employee"""
        return f"Employee Name: {self.name}, Salary: {self.salary}"


class Coder(Employee):

    """Coder class"""
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

    def get_details(self):
        self.salary += 10000  # Coders get a bonus

        return (
            f"Employee Name: {self.name}, "
            f"Salary: {self.salary}, "
            f"Programming Language: {self.programming_language}"
        )


class Designer(Employee):

    """Designer class"""
    def __init__(self, name, salary, design_tool):
        super().__init__(name, salary)
        self.design_tool = design_tool

    def get_details(self):
        self.salary += 5000  # Designers get a bonus
        return (
            f"Employee Name: {self.name}, "
            f"Salary: {self.salary}, "
            f"Design Tool: {self.design_tool}"
        )


EMPLOYEES = [Employee("Alice", 70000), Coder("Bob", 90000, "Python"),
             Designer("Charlie", 80000, "Photoshop")]

for emp in EMPLOYEES:
    print(emp.get_details())
