# I want to model an organization. An organization models the relationships between
# employees. Each employee has a name, and all but one of the
# employees (the CEO) has a manager. Please write a class to model this.

class Organization

    def __init__(self, employees=dict):
        self.employees = employees

    def find_managers(self):
        managers = []
        for id, employee in employees.items():
            if employee.manager:
                manager.append(employee.manager)
        return managers


class Employee:
    def __init__(self, name, employees  # list):
        self.name = name

    self.employees = employees

    ###
    ceo = Employee(1, 'a', null)
    manager_one = Employee(2, 'b', ceo.name)
    employees = {
        ceo.id: ceo,
        manager.id: manager
    }
    organization = Organization(employees)

    employees = organization.employees

    for id, employee in employees.items():
        if
    employee.manager: \
        print(employee.manager)

    # 1 ceo "Mark"
    #  - 1 manager
    #    - 2 employees
    #  - 1 manager "Bob"
    #    - 1 employee = "Jim"
    # printChain("Jim") -> "Jim", "Bob", "Mark"


def print_chain(name):
    employees = organization.employees

    current_employee = employees[name]  # id
    res = []
    while current_employee:
        res.append(current_employee.name)
        manager = current_employee.manager
        # manager = current_employee
        current_employee = employees[manager]

    return res


name = 'Jim'
print_chain(name)


# Let's say that I've created an organization tree using your class, and
# I'm going to give you the root node (the CEO). Can you write a method
# to find the highest degree of separation from the root node (CEO)?


#
class Employee:
    def __init__(self, name, employees  # list):
        self.name = name

    self.employees = employees


def find_highest_degree(root):
    degree = 0

    def find_employee(node):
        if not node:
            return 0
        employees = node.employees
        degrees = []
        for employee in employees:
            degrees.append(find_employee(employee))

        return 1 + max(degress)

    degree = find_employee(root)
    return degree


ceo = root  ##
find_highest_degree(ceo)

O(n)
O(n)

# Given two employees, can you write a method to find their lowest common
# manager?

