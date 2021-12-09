from person import Person
from person import Gender
from department import Department


class Employee(Person):
    def __init__(self, lastname: str = "", firstname: str = "", age: int = 0,
                 gender: Gender = Gender.NONE_SPECIFIED,
                 department: Department = Department.NONE_SPECIFIED):
        super(Person, self).__init__(lastname, firstname, age, gender)
        self.department = department

    def __str__(self):
        return super(Person, self).to_string() + "\ndepartment: " + self.department.value
