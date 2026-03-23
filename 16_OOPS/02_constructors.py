class Employee:

    def __init__(self, name, salary, bond):
        self.name = name  # create an instance attribute name, salary and assign it with salary
        self.salary = salary 
        self.bond = bond

    def get_salary(self):
        return self.salary
    
    def get_info(self):
        print(f"The name of the Employee is {self.name}. The Salary is {self.salary} and bond is for {self.bond} year")


e1 = Employee("Shyam", 1225, 5)
print(e1.get_salary())
e1.get_info()