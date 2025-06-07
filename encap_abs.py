# Abstraction : hiding the implementation details of a class and only showing the essential features to the user

class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.clutch = True
        self.acc = True
        print("Car Started...")

c1 = Car()
c1.start()
'''Encapsulation : Wrapping data and fucntions into a single unit(object)
          capsule = data + functions

    access modifiers : 
          public - 
          private - attributes and methods are accessible inside class only - represented as "__"(double underscores)
          protected - 
          default
'''

# create Account class with 2 Attributes - balance & account number. Create methods for debit,credit & printing the balance
class Account:
    def __init__(self,balance,acc_no,acc_pass):
        self.balance = balance
        self.acc_no = acc_no
        self.__acc_pass = acc_pass

    def debit(self,amount):
        self.balance = self.balance - amount
        print("Rs.",amount,"has been debited from your account!")

    def credit(self,amount):
        self.balance = self.balance + amount
        print("Rs.",amount,"has been credited to your account!")

    def print_bal(self):
        print("Your current balance is",self.balance)

a1 = Account(55000,451236,54132)
a1.debit(2500)
a1.print_bal()
a1.credit(9000)
a1.print_bal()
print(a1.__acc_pass) # won't be accessible as it lies outside the class!!