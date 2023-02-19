print('The isinstance')

class MyCat:
    def __init__(self, name, fvtFood):
        self.catName = name
        self.CatFvtFood = fvtFood

cat1= MyCat('Lucy', 'beans')
print(cat1.__dict__)
print(isinstance(cat1, MyCat))