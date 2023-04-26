class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

class Employee:
    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department

it_dept = Department("IT")
john = Employee("John", 30, it_dept)
jane = Employee("Jane", 25, it_dept)
it_dept.add_employee(john)
it_dept.add_employee(jane)

for employee in it_dept.employees:
    print(employee.name)
