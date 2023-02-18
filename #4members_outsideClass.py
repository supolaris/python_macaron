print("Class members outside the class")

class Cars:
    def __init__(self, name, model):
        self.carname = name
        self.carmodel = model

    def display(self):
        print(f"The car name is {self.carname} and car model is {self.carmodel}")

car1=Cars('honda', 'city')


#car1.attribure_name
#car1.action_name()

#accessing attributes outside the class
car1.carname = 'Honda'
print(car1.carname)
print(car1.carmodel)

#accessing action outside the class
car1.display()
