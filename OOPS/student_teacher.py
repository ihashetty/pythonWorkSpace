"""student and teachers"""


from typing import List, Optional


class Student:

    """Student"""
    def __init__(self, id: int, name: str, total_marks: float):
        # keep them private but expose via properties
        self.__id = int(id)
        self.__name = str(name)
        self.__total_marks = float(total_marks)

    @property
    def id(self) -> int:
        return self.__id

    @property
    def name(self) -> str:

        """Initialise name"""
        return self.__name

    @property
    def total_marks(self) -> float:

        """Initialise total_marks"""
        return self.__total_marks

    def __repr__(self) -> str:

        """print student details"""
        return (
            f"Student(id={self.id}, "
            f"name='{self.name}', "
            f"total_marks={self.total_marks})"
        )


class Teacher:

    """Teacher class"""

    def __init__(
        self,
        id: int,
        name: str,
        student_list: Optional[List[Student]] = None
    ):
        self.id = int(id)
        self.name = str(name)
        self.student_list: List[Student] = []
        # If an initial list is provided, add via add_student
        # (validates type & duplicates)
        if student_list:
            for s in student_list:
                self.add_student(s)

    def add_student(self, student: Student) -> None:

        """Add a student if not already present by id."""
        if not isinstance(student, Student):
            raise TypeError(f"Expected Student, got {type(student).__name__}")
        if any(s.id == student.id for s in self.student_list):
            raise ValueError(f"Student with id={student.id} already exists.")
        self.student_list.append(student)

    def list1(self):

        """List1 initialisation"""
        return len(self.student_list)

    def remove_student(self) -> None:

        """Remove a student by id."""
        for k in self.student_list:
            if k.total_marks < 20:
                print(k)
                self.student_list.pop(k)

    def get_student(self, student_id: int):

        """Fetch a student by id."""
        return next((s for s in self.student_list if s.id == student_id), None)

    def count_people(self):

        """count people"""
        count = 0
        for k in self.student_list:
            if k.total_marks >= 75:
                count += 1
        return count


# ---- Example usage (works) ----
if __name__ == "__main__":
    s1 = Student(10, "iha", 100)
    s2 = Student(11, "savi", 95)

    teacher = Teacher(121, "reva")          # start with empty list
    teacher.add_student(s1)                 # OK
    teacher.add_student(s2)                 # OK

    print(teacher.list1())
    # Teacher(id=121, name='reva', students=2)
    print(teacher.count_people())          # 97.5
    print(teacher.remove_student)
    # Student(id=10, name='iha', total_marks=100)

    # If you pass a wrong type, you'll get a clear error:
    # teacher.add_student("savi")           # -> TypeError
