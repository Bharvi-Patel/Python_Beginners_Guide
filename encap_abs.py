# Abstraction : hiding the implementation details of a class and only showing the essential features to the user
'''Encapsulation : Wrapping data and fucntions into a single unit(object)
          capsule = data + functions

          access modifiers
          public
          private
          protected
          default
'''

# create Account class with 2 Attributes - balance & account number. Create methods for debit,credit&printing the balance
class Account:
    def __init__(self,balance,acc_no):
        self.balance = balance
        self.acc_no = acc_no

    def debit(self,amount):
        self.balance = self.balance - amount
        print("Rs.",amount,"has been debited from your account!")

    def credit(self,amount):
        self.balance = self.balance + amount
        print("Rs.",amount,"has been credited to your account!")

    def print_bal(self):
        print("Your current balance is",self.balance)

a1 = Account(55000,451236)
a1.debit(2500)
a1.print_bal()