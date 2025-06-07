# Decorators : allows us to wrap another function in order to extend the behaviour of the wrapped function,without permanently modifying it


# Static Methods : Methods that don't use the self parameter(works at class level)

class Student:
    @staticmethod               
    def college():
        print("falanaDhimkana")

s1 = Student()
s1.college()

# Class Methods : A class method is bound to the class & recieves the class as an implicit first argument.
'''
NOTE - static method can't access or modify class state & generally for utility.
'''
class Person :
    name = "anonymous"
    
    # def changeName(self,name):
    #     self.name = name # this create new instance attribute name ; doesn't changes the name attribute of the class
    #     Person.name = name # this will update the name attribute of the class 
    #     self.__class__.name = "Raju sriwastav" # using __class__ method

    @classmethod
    def changeName(cls,name):
        cls.name = name
    
p1 = Person()
p1.changeName("Raju Sriwastav")


# Property Decorator : we use property decorator on any method in the class to use the method as a property
class Kid():
    def __init__(self,phy,maths,chem):
        self.phy = phy
        self.maths = maths
        self.chem = chem

    @property
    def percentage(self):
        return str((self.phy + self.chem + self.maths)/3) + "%"
        
k1 = Kid(60,36,50)
print(k1.percentage)
k1.maths = 66
print(k1.percentage)

# jab bhi dusre parameter mein change hoga...wo change automatically refelct ho jayega if @property used!
# here,when the maths's marks were updated,we did not need to manually write the code to recalculate the percentage with updated data...as we used @property
#  decorator,this was done automatically...@property decorator converts the attributes/variables into properties