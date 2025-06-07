import math

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

    cust2 = Customer("Bharvi","Female")
    return cust2

cust = Customer("Bharvii","female")

new_cust = greet(cust)
print(new_cust)


# EXAMPLE - 1
# Define a Circle class to create a circle with radius r uaing the constructor. Define an Area() method of the clas which calculates 
# the area of the circle. Define a Perimeter() method of the class which allows you to calculate the perimeter of the cirle.

class Circle:
    def __init__(self,radius):
        self.radius = radius

    def Area(self):
        area = math.pi * self.radius * self.radius
        print("Area of the circl is",area )

    def Perimeter(self):
        perimeter = 2 * math.pi * self.radius
        print("Perimeter of the circle is",perimeter)

circle1 = Circle(6)
circle1.Area()
circle1.Perimeter()


# EXAMPLE - 2
# Define a Employee class with attributes role,department & salary. This class also has a  showDetails() method. Create an Engineer class 
# that inherits properties from Employee & has additional attirbutea : name & age.

class Employee():
    def __init__(self,role,dept,salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def showDetails(self):
        print("Role =",self.role)
        print("Department=",self.dept)
        print("Salary=",self.salary)

class Engineer(Employee):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        super().__init__("Engineer","IT",5000000)

e1 = Employee("Analyst","Analysis","65000")

e1.showDetails()

e2 = Engineer("Jethalal Champaklal Gada","35")
print("Name =",e2.name,"  Age =",e2.age)
e2.showDetails()


# EXAMPLE - 3
# Create a class called Order which stores item & it's price. Use dunder function __gt__() to convey that :
#                                                             order1 > order2 if price of order1 > price of order2    ; gt = greater than

class Order:
    def __init__(self,item,price):
        self.item = item
        self.price = price

    def __gt__(self,order2):
        return self.price > order2.price

order1 = Order("cookies",40)
order2 = Order("Ice-Cream",60)

print(order1 > order2)