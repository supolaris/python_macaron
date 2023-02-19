class Parent:
    bookName = 'The last source'



class Child(Parent):
    def bpages(self):
        bookPages = 1235



b1 = Parent()
b2 = Child()

print(b2.bookName)
