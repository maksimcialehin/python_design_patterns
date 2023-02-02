from abc import ABCMeta, abstractmethod


class IDepartment(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self, employees):
        """ Implement in child class """

    @staticmethod
    @abstractmethod
    def print_department():
        """ Implement in child class """


class Accounting(IDepartment):

    def __init__(self, employees):
        self.employees = employees

    def print_department(self):
        print(f'Accounting department: {self.employees}')


class Development(IDepartment):

    def __init__(self, employees):
        self.employees = employees

    def print_department(self):
        print(f'Development department: {self.employees}')


class ParentDepartment(IDepartment):

    def __init__(self, employees):
        self.employees = employees
        self.base_employees = employees
        self.sub_depts = []

    def add(self, dept):
        self.sub_depts.append(dept)
        self.employees += dept.employees

    def print_department(self):
        print(f'Parent department')
        print(f'Parent Department base employees: {self.base_employees}')
        for dept in self.sub_depts:
            dept.print_department()
        print(f'Total number of employees: {self.employees}')



dept1 = Accounting(20)
dept2 = Development(17)

main_dept = ParentDepartment(8)
main_dept.add(dept1)
main_dept.add(dept2)
main_dept.print_department()
