from person import Person
from person import Gender


class Leader:
    def __init__(self, group, person_id, name, age, gender=Gender.NotSpecified):
        self.group = group
        self.person_id = person_id
        self.name = name
        self.age = age
        self.gender = gender
