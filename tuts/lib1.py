from abc import ABCMeta, abstractstaticmethod
class IProvider(metaclass=ABCMeta):
    @abstractstaticmethod
    def print_data():
        """ implement in child class """

class Provider(IProvider):
    __instance = None

    @staticmethod
    def get_instance():
        if Provider.__instance is None:
            Provider("Universal Provider", 0)

        return Provider.__instance

    def __init__(self, name, count=0):
        if Provider.__instance is not None:
            raise Exception("Singleton cannot be instantiated more than once")
        self.name = name
        self.count = count
        Provider.__instance = self

    @staticmethod
    def print_data():
        print(f"Name: {Provider.__instance.name}")


# test Provider
univ = Provider.get_instance()
univ.print_data()

######## Composite Patterns ##############

class IDepartment(metaclass=ABCMeta):
    @abstractstaticmethod
    def __init__(self, employees):
        """ implement in child class """

    @abstractstaticmethod
    def print_department(self):
        """ implement in child class """

class Accounting(IDepartment):

    def __init__(self, employees):
        self.employees = employees

    def print_department(self):
        print(f"Accounting department : {self.employees}")


class Development(IDepartment):

    def __init__(self, employees):
        self.employees = employees

    def print_department(self):
        print(f"Accounting department : {self.employees}")

class ParentDepartment(IDepartment):
    def __init__(self, employees):
        self.employees = employees
        self.base_employees = employees
        self.sub_depts = []

    def add(self, dept: IDepartment):
        self.sub_depts.append(dept)
        self.employees += dept.employees

    def print_department(self):
        print("Parent Department")
        print(f"Parent Department Base Employee: {self.base_employees}")
        for dept in self.sub_depts:
            dept.print_department()
        print(f"Total number of employees: {self.employees}")


#### Test Departments ###
dept1 = Accounting(200)
dept2 = Development(100)
parent_dept = ParentDepartment(30)
parent_dept.add(dept1)
parent_dept.add(dept2)
parent_dept.print_department()
