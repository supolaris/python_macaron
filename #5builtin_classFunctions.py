print("Builtin Class Functions")

class Fruits:
    def __init__(self, name, origin, color):
        self.fName = name
        self.fOrigin = origin
        self.fColor = color

fruit1= Fruits('Mango', 'Pakistan', 'Yellow')
print(fruit1.__dict__)
print(fruit1.fName)

#getattribute (object, variable)
print(getattr(fruit1, 'fColor'))

#setattribute (object, variable, newvalue)
setattr(fruit1, 'origin', 'Maldives')
print(fruit1.__dict__)

#delattribue (object, variable)
delattr(fruit1,'origin')
print(fruit1.__dict__)

#hasattribute (object, variable)
print(hasattr(fruit1, 'origin'))
