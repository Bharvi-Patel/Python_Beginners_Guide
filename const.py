# Constructors : All class have a function called __init__(),which is always executed when the object is being initiated

class Car:
    year = "2004"#class attribute
    brandName = "Anonymous" 

    # constructors always take one parameter called "self" , if not given...it would give error
    def __init__(self):# default constructors
        print("Give up on your dreams and die.")

        '''self parameter : is a reference to the current instance of the class,and is used to access variables that belongs to the class
        (we can use anything instead of self e.g star)'''
    
    def __init__(self,color,brandName):# parameterized constructors
        print("Learning...")
        self.color = color
        self.brandName = brandName
        
        # Methods : functions that belongs to objects
    def hello(self): # har method mein self use karna hi hai
        print("been a long time...")

c1 = Car("Red","Mercedes")
print(c1.color , "color car of",c1.brandName)

c2 = Car("White","BMW")
print(c2.color,"color car of",c2.brandName)

# Class Attributes : Variables defined inside class ,outside of any constructor
# Instance Attributes : inside constructors
# Object Attribute > Class Attribute

print(Car.year) # and print(s1.year) - both prints the same thing
print(c1.brandName) #Mercedes will be printed!!!!


# Method calling
c1.hello()


# Create student class that takes name & marks of 3 subjects as arguments in constructor. Then create a method to print the average.
class Student:
    def __init__(self,name,marks): #marks is a list
        self.name = name
        self.marks = marks

    def avg(self):
        sum = 0
        for i in self.marks:
            sum += i
        print("Greetings,\n",self.name,"Your avg score is :",sum/3)

s1 = Student("Betty",[87,79,92])
s1.avg()

s2 = Student("Joker",[65,75,78])
s2.avg()