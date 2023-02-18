class Employee:
    def __init__(self, sal, age):
        # self variable holds the address location for variable sal and age.
        self.salary = sal
        self.age = age

e1=Employee(2400, 24)
print(e1.__dict__)

