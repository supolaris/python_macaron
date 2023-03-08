class Teacher:
    def __init__(self):
        print("I am teacher")
        self.var = "Teacher teach the students"

class Student(Teacher):
    def __init__(self):
        print("I am student")
        self.var2 = "Student are being teached by teacher"


s1=Student()
print(s1.__dict__)