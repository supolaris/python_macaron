print("Builtin Class Attributes")

class MyHOuse:
    '''Anything written in three quotation marks and within class shows in __doc__ builtin attribute'''
    def __init__(self, Country, City):
        self.myCountry = Country
        self.MyCity = City


House1=MyHOuse('Pakistan', 'Islamabad')

# __doc__ prints the message within ''' '''
print(MyHOuse.__doc__)

#__dict__ prints the whole things of class
print(MyHOuse.__dict__)

#__name__ prints the name of class
print(MyHOuse.__name__)

#__module__ prints the module name
print(MyHOuse.__module__)