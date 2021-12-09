import enum
import company

class Gender(enum.Enum):
    Male = 1
    Female = 2
    NotSpecified = 3


class Person:
    def __init__(self, personId, name, age, gender, department):
        super(company).__init__(department)
        self.personId = personId
        self.name = name
        self.age = age
        self.gender = gender

    def gender(self):
        pass

    def department(self):
        pass

    def __str__(self):
        pass
