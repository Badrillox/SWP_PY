from employee import Employee
from leader import Leader
from person import Person
from person import Gender
from company import Company
from department import Department
if __name__ == "__main__":
    empty_person = Person()
    person = Person(1, "Jackson", "Kevin", 19, Gender.Male, Department.Development)
    empty_worker = Employee()
    worker = Employee("Perktold", "Michael", 19, Gender.Male, Department.Development)
    #subordinates = [person, worker]
    worker.to_string()
    empty_group_leader = Leader();
    group_leader = Leader("Baumgartner", "Torben", 20, Gender.Male, Department.LogisticsTec)
    people: list = [empty_person, person]
    workers: list = [empty_worker, worker]
    group_leaders: list = [empty_group_leader, group_leader]
    all_people: list = people + workers + group_leaders

    for temp_person in all_people:
        print("\n\t" + temp_person.to_string())

    print()
    company = Company(empty_worker, group_leaders)
    # print("Amount of worker\t: " + company.amount_of_worker())
    # print("Amount of group-leaders\t: " + company.amount_of_group_leader())
    print("Amount of departments\t: " + str(company.amount_of_departments()))
    print("departments\t: ")
    for dep in company.find_departments():
        print("\t" + dep.value)
    print()
    temp_dict = company.find_amount_of_participates_per_departments()
    for temp_key in temp_dict:
        print(temp_key.value + "\t: " + str(temp_dict[temp_key]))

    print("\nDepartment with the most workers")
    temp_dict = company.find_biggest_department()
    for temp_key in temp_dict:
        print(temp_key.value + "\t: " + str(temp_dict[temp_key]))

    print("\nGender-spreading")
    gender_spreading = company.gender_spread()
    for s in gender_spreading:
        print(s.value + "\t" + str(gender_spreading[s]))