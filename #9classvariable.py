print("Class variable")

class NewClass():
    Variable = "New variable"
    def __init__(self, name):
        self.myname = name

    @classmethod
    def get_classVariable(cls):
        NewClass.Variable= input("Enter new value")
        print(NewClass.Variable)

clas1=NewClass('suleman')

# the class variable is only accessed by the class itself and the objects
print(NewClass.Variable)
print(clas1.__dict__)
NewClass.get_classVariable()