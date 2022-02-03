from department import Department
from person import Person
from person import Gender
from employee import Employee


class Leader(Employee):
    def __init__(self, group="", person_id=0, lastname="", firstname="", age=0, gender=Gender.NotSpecified,
                 department=Department.NotSpecified):
        self.group = group
        self.person_id = person_id
        self.lastname = lastname
        self.firstname = firstname
        self.age = age
        self.gender = gender
        super().__init__(lastname, firstname, age, gender, department)

    def __str__(self):
        return super(Leader, self).__str__()
