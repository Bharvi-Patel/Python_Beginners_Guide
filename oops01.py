# OOPS - Object Oriented Programming Structure , a way of organizing code that uses objects and classes to represent real-world entities and their behavior
'''
oop concepts : object,class,polymorphism,encapsulation,inheritance,abstraction
'''
# Class - A class is a collection of objects. Classes are blueprints for creating objects.
# A class defines a set of attributes and methods that the created objects (instances) can have.

'''
    class - data or property/methods
          - functions or behavior
''' 
# class example
class Car :
    color = "red"
    model = "sports"
    def calculate_avg_speed(self,km,time):
        pass# here would be some code(added pass to avoid unnecessay errors)

# Object - Object is an instance of a class
wagnor = Car()
'''
 *python mein har ek chiz object hai pr object kisi class ka hi ho skta hai*
 *in python,datatype is a class and when me declare variable in our code it's actually object of that class eg. a=10(a is object of int class)*
 '''
        

# ATM Class 
class Atm:
    def __init__(self): #variable in the class must be declared inside this method
        self.__pin = ""
        self.__balance = 0
        self.amount=0
        self.menu()

    def get_pin(self):
        return self.__pin

    def set_pin(self,new_pin):
        self.__pin=new_pin
        print("Pin Changed!")    

    def __menu(self):                                       # we can hide methods as well
        user_input = input("""
                        Hello,how would you like to proceed?
                        1.Enter 1 to create pin
                        2.Enter 2 to deposit
                        3.Enter 3 to withdraw
                        4.Enter 4 to check balance
                        5.Enter 5 to exit
        """)

        if user_input =="1":
            self.create_pin()
        elif user_input=="2":
            self.deposit()
        elif user_input=="3":
            self.withdraw()
        elif user_input=="4":
            self.check_balance()
        else:
            print("Exit")

    def create_pin(self):
        self.__pin = input("Enter your pin : ")
        print("Pin set successfully!")

    def deposit(self):
        temp = input("Enter your pin : ")
        if temp == self.__pin:
            self.amount = int(input("Enter the amount : "))
            self.__balance = self.__balance + self.amount
            print("Deposit successfull!")
        else:
            print("Invalid Pin")

    def withdraw(self):
        temp = input("Enter your pin : ")
        if temp == self.__pin:
            self.amount = int(input("Enter the amount : "))
            if self.amount<self.__balance:
                self.__balance = self.__balance - self.amount
                print("Operation Successfull")
            else:
                print("Insufficient funds")
        else:
            print("Invalid Pin")

    def check_balance(self):
        temp = input("Enter your pin : ")
        if temp == self.__pin:
            print(self.__balance)
        else:
            print("Invalid Pin")


SBI = Atm()
# SBI.menu()
SBI.create_pin()
SBI.deposit()
SBI.check_balance()
SBI.withdraw()

# constructor - special method jiska code automatically execute hota hai jaise hai uss class ka object banaye - __init__ (this should always be the constructor)
# **Functions** are just normal functions whereas **Method** are functions inside the class


# Magic Method - aage peeche double underscore (__).These are predefined.These are special methods/dunder methods which are automatically triggered.
#              - object call nai karta inko,ye khud call ho jaate hai
#              -__add__,__sub__

# self - ek class ka ek method apne class ke dusre method se baat naii kar sakta(__init__,menu ko call naii kar sakta),iske liye hume ek object chahiye
#      - self is basically the current object
'''
function - len(L)(class ke bahar defined hoga)
method   - L.append(5) (because append might be the function of the List class)
'''

# can directly call this file as module in comand promt - from oops01 import Atm

# Instance Variable - variables inside the constructors,value of the variable is different for differet objects 

'''
    Encapsulation - Data Hiding
                    internally -  while running Atm,whenever interpreter came across" __" it replaces that with _Atm__pin(for eg) 
                                                                                                    then we can't access __ variable or method
                    *Nothing in python is truly private* 
                    one can access private variable with "SBI._Atm__balance=545445"(if they know that this variable exist,then it can be easily accessed )
                    
         
                                                                                                        
'''