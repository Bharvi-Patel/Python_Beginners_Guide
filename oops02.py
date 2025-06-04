# passing class object as argument to the function

class Customer:
    def __init__(self,name,gender):
        self.name = name 
        self.gender = gender

def greet(customer):
    if customer.gender == "Male":
        print("Hello",customer.name,"sir")
    else:
        print("Hello",customer.name,"ma'am")

    cust2 = Customer("Bharvi","Fem8ale")
    return cust2

cust = Customer("Bharvii")

new_cust = greet(cust)
print(new_cust)

