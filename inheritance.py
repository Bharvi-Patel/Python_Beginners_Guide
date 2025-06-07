# Inheritance : one class(child class) inherits properties & methods of another class(parent class)
'''
class ParentClass():
    -
    -
    -
class ChildClass(ParentClass)
    -
'''

class Singer():
    def __init__(self,age,YearsOfCareer):
        self.age = age
        self.year = YearsOfCareer

    @staticmethod
    def professionals():
        print("All of these are professional and very successfull singers.")

class TaylorSwift(Singer): # Single Inheritance
    def albums(self):
        print("She has made total of 12 albums throughout her career.")

class Midnights(TaylorSwift):# Multi-line Inheritance
    def songs(self):
        print("Midnights ais Taylor Swift's 11th charts and records breaking album.")

# class MidnightRain(TaylorSwift,Midnights):  Multiple Inheritance
#     def mean(self):
#         print("Midnight Rain is the song by Singer - Songwriter and a Billionair(Through her music only) TAYLOR SWIFT")


s1 = TaylorSwift(35,20)
s1.professionals()
s2 = Midnights(25,20)
s2.albums()
s2.songs()
# s2.mean()

'''
Types :
 (i)   Single Inheritance : Parent --> Child
 (ii)  Multi-levvel Inheritance : GrandParent --> Parent --> Child
 (iii) Multiple Inheritance : Parent1 + Parent2 --> Child
                              e.g class Parent1():
                                  class Parent2():
                                  class Child(Parent1,Parent2):
''' 


# Super method : Super() method is usedd to access methods of the parent class
class Car:
    def __init__(self,type):
        self.type = type

    @staticmethod
    def start():
        print("Car Started.")

    @staticmethod
    def stop():
        print("Car stopped.")

class ToyotaCar(Car):
    def __init__(self,name,type):
        self.name = name
        super().__init__(type)
        super().start()

c11 = ToyotaCar("Fortuner","fuel")
print(c11.type)
print(c11.name)
# c11.start()