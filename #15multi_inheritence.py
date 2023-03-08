class Student(object):
    def __init__(self):
        self.name= input("Enter the student name")
        self.roll = 627

class Teacher(Student):
    def __init__(self):
        self.name= input("Enter the teacher name")
        self.tid = 557

class Principle(Teacher):
    pass

p1 = Principle()
