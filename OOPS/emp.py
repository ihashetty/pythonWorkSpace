"""emp doc"""


class Employee:

    """Employee class"""
    def __init__(self, id=None, name=None, salary=None):
        self.__id = id
        self.__name = name
        self.__salary = salary

    def get_id(self):

        """get id"""
        return "The id is : "+self.__id

    # def get_no_of_teams(self):
    #     return self.__no_of_teams
    def show_details(self):

        """show details"""
        print(self.__id, self.__name, self.__salary)


class Manager(Employee):

    """Manager class"""
    def __init__(self, id=None, name=None, salary=None, no_of_teams=None):
        super().__init__(id, name, salary)
        self.__no_of_teams = no_of_teams

    def show_details(self):

        """show details """
        super().show_details()
        print(self.__no_of_teams)


emp = Employee("101", "Neo", 50000)
emp.show_details()
mgr = Manager("201", "Smith", 80000, 5)
mgr.show_details()
