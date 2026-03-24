class Employee:

    company = "Citadel" # class attribute

    def __init__(self, name, salary, bond, company):
        self.name = name
        self.salary = salary
        self.bond = bond
        self.company = company

    def get_salary(self):
        return self.salary

    def get_info(self):
        print(f"The name of the Employee is {self.name}. The Salary is {self.salary} and bond is for {self.bond} year")


e1 = Employee("Shyam", 1225, 5, "Tower Research Capital") 
print(e1.company) # will always print instance attribute whenever present
print(Employee.company) # will always print class attribute

# Object Introspection
print(dir(e1))