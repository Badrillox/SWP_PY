import collections
import copy

from person import Gender
from department import Department


class Company:
    def __init__(self, employee, group_leaders, department=Department.NotSpecified, name=""):
        self.department = department
        self.name = name
        self.employee = employee
        self.group_leaders = group_leaders

    def amount_of_worker(self):
        return self.employee is not None if len(
            self.employee) else 0

    def amount_of_group_leader(self):
        return self.group_leaders is not None if len(
            self.group_leaders) else 0

    def amount_of_departments(self):
        return len(self.find_departments())

    def find_departments(self):
        return self.sub_find_departments(self.employee) + self.sub_find_departments(self.group_leaders)

    def sub_find_departments(self, people):
        departments: list = []
        if people is not None:
            for person in people:
                is_in_list = False
                if len(departments) != 0:
                    for d in departments:
                        if person.department is d:
                            is_in_list = True
                            break
                if is_in_list is False:
                    departments.append(person.department)
        return collections.Counter(departments)

    def find_amount_of_participates_per_departments(self):
        temp_worker = self.group_leaders + self.employee
        temp_dict: dict = {}
        for d in self.find_departments():
            temp_dict[d] = 0
        for employee in temp_worker:
            temp_dict[employee.department] = temp_dict[employee.department] + 1
        return temp_dict

    def find_biggest_department(self):
        dict = copy.deepcopy(self.find_amount_of_participates_per_departments())
        sorted_dict = sorted(dict.items(), key=lambda x: x[1], reverse=True)
        new_dict = {}
        for d in sorted_dict:
            if len(new_dict) == 0:
                new_dict[d[0]] = d[1]
            else:
                if new_dict[list(new_dict)[-1]] == d[1]:
                    new_dict[d[0]] = d[1]
                else:
                    break

        return new_dict

    def gender_spread(self):
        people = self.employee + self.group_leaders
        spreading = {}
        for g in Gender:
            spreading[g] = 0
        for p in people:
            spreading[p.gender] = spreading[p.gender] + 1
        return spreading

    pass
