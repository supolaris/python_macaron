class BMW:
    def carDetails(self):
        print("Fuel type is diesel")

    def speed(self):
        print("Speed in 300 kmh")

class Ferarri:
    def carDetails(self):
        print("Fuel type is petrol")

    def speed(self):
        print("Speed is 200 kmh")

def display(obj):
    obj.carDetails()
    obj.speed()

car1 = BMW()
car2 = Ferarri()

display(car1)
print("-----------")
display(car2)