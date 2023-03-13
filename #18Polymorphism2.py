class Student:
    def __init__(self, name, roll, dept):
        self.sname = name
        self.sroll = roll
        self.sdept = dept

    def display(self):
        print("Student name is: ", self.sname)
        print("Student roll is: ", self.sroll)
        print("Student department is: ", self.sdept)

    def library(self):
        print(self.sname, " has enrolled 5 books")

    def canteen(self):
        print(self.sname, " has bill of 1500 pkr")

class Student2(Student):
    def library(self):
        print(self.sname, " has enrolled 9 books")

    def canteen(self):
        print(self.sname, " has bill of 2500 pkr")


s1 = Student("Bond", 500, "UUII")
print(s1.display())
s2 = Student2("James", 70, "AARR")
print(s2.display())