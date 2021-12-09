import enum
import company
import department as dp

class Gender(enum.Enum):
    Male = 1
    Female = 2
    NotSpecified = 3


class Person:
    def __init__(self, person_id, name, age=0, gender=Gender.NotSpecified,
                 department=dp.Department.NotSpecified):
        self.personId = person_id
        self.name = name
        self.age = age
        self.gender = gender
        self.department = department

    def __str__(self):
        return "Name: " + self.name + "\nage\t: " + self.age + "\ngender\t: " + self.gender + "\ndepartment\t: " + self.department
