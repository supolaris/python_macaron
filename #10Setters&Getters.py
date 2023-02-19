print("The setter and getter method")

class Employees:
    def setName(self, name, id):
        self.myName = name
        self.myId = id

    def getName(self):
        print("the name is: ", self.myName, " and the roll number is: " , self.myId)

e1 = Employees()
e2 = Employees()
e3 = Employees()

e1.setName(input("Enter the name : "), int(input("Enter the id: ")))

e1.getName()