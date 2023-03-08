class Teacher:
    def __init__(self, name, clas):
        self.tname = name
        self.tclass = clas
        print("This is teacher here")

    def newFun(self):
        print("this is another constructor")

class Student(Teacher):
    def __init__(self, name, clas):
        super().__init__(name, clas)
        super().newFun()
        print("this is student here")

s1 = Student('ali',  632)
print(s1.__dict__)
