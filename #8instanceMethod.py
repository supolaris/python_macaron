print("The instance method")

class MySelf:
    def __init__(self, name, roll):
        self.myName = name
        self.myRoll = roll

    def getUpdate(self):
        self.myName = (input("Enter the new name: "))
        self.myRoll = (int(input("Enter the new roll number: ")))

    def diplay(self):
        print("Your new name is : " + self.myName + "Your new roll number is: " + str(self.myRoll))

    @classmethod
    def get_classVAr(cls):
        classVar = input("Enter the new value")

nn = ("Your name is Suleman")
bb = ("Your roll number is 627")
self1 = MySelf(nn, bb)
print(self1.__dict__)
self1.getUpdate()
self1.diplay()


