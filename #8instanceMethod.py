print("The instance method")

class MySelf:

    def __init__(self, name, roll):
        self.myName = name
        self.myRoll = roll

    def getUpdate(self):
        self.myName = print(input("Enter the new name: "))
        self.myRoll = print(int(input("Enter the new roll number: ")))

    def diplay(self):
        print(self.myName, self.myRoll)

nn = ("Your name is Suleman")
bb = ("Your roll number is 627")
self1 = MySelf(nn, bb)

self1.diplay()
self1.getUpdate()
print(self1.__dict__)

