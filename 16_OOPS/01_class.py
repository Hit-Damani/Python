# class is a template like a blueprint 
# Object is a specific instance created from a class

class Employee:
    company_name = "Tower Research Capital"

    def get_salary(self): # self is important bcoz self is a way to reference the object of the class which is being created
        return 25000

e1 = Employee() # an object of class Employee is created
print(e1.get_salary()) # Employee get_salary method is called
print(e1.company_name, end="\n\n")

e2 = Employee()
print(e2.get_salary()) # Employee get_salary method is called
print(e2.company_name)