# class - blueprint for creating objects
class Student:
    name = "Bharvi Patel"

# objects - instance of a class 
s1 = Student()
print(s1)
print(s1.name)

# car factory
class Car:
    color = "Red"
    
c1 = Car()
print(c1.color)

# del keyword : used to delete object properties or object itself
del s1.name
del s1