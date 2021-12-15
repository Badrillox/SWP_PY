import enum

import department as dp


class Gender(enum.Enum):
    Male = 1
    Female = 2
    NotSpecified = 3


class Person:
    def __init__(self, person_id=0, lastname="", firstname="", age=0, gender=Gender.NotSpecified,
                 department=dp.Department.NotSpecified):
        self.personId = person_id
        self.lastname = lastname
        self.firstname = firstname
        self.age = age
        self.gender = gender
        self.department = department

    def __str__(self):
        return "Name: " + self.name + "\nage\t: " + self.age + "\ngender\t: " + self.gender + "\ndepartment\t: " + self.department
