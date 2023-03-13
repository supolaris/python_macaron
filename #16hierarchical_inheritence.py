class Student(object):
    def __init__(self, name, age):
        self.sname = name
        self.sage = age

class Teacher(Student):
    def __init__(self, name, age, sal):
        self.tsal = sal

class Principle(Student):
    def __init__(self, name, age, id):
        super.__init__(name, age)
        self.pid = id

p1 = Principle('ali', 12, 21)
print()
