from department import Department


class Company:
    def __init__(self, department=Department.NotSpecified, name=""):
        self.department = department
        self.name = name
