from person import Person
from person import Gender
from department import Department


class Employee(Person):
    def __init__(self, lastname="", firstname="", age: int = 0,
                 gender=Gender.NotSpecified,
                 department=Department.NotSpecified):
        super().__init__(lastname, firstname, age, gender)
        self.department = department

    def __str__(self):
        return super(Person, self).__str__() + "\ndepartment: " + str(self.department.value)
