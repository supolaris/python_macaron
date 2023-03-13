class MyClass:
    def __init__(self, name, dept, loc):
        self.cname = name
        self.cdept = dept
        self.cloc = loc
    def display(self):
        print(self.cname, self.cloc, self.cdept)

    def __len__(self):
       return len(self.cname)+len(self.cloc)+len(self.cdept)

myObj = myClass(["II, CS"], ["UIIT", "UMS"], ["Stadium", "Road"])
print(myObj.display())
print(myObj.__len__())
