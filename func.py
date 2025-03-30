# Functions - group of statements performing a specific task
# def - (keyword)is used to define a function
def hello():
    print("Hiii,How you doing?")
hello()# function calling

# Return Statement - A return statement is used to end the execution of the function call and 
# it “returns” the value of the expression following the return keyword to the caller
# The statements after the return statements are not executed. 
# If the return statement is without any expression, then the special value None is returned

# Parameters and Arguments
# Parameters - Parameters are variables defined in a function declaration
# Arguments - Arguments are the actual values that you pass to the function when you call it

def add(a, b): # a,b are paratmers
    # returning sum of a and b
    return a + b

def sub(x, y):
    return (x-y)
print(add(4,5))# 4,5 are arguments
print(sub(9,5))



# Parameters and Arguments
# Parameters - Parameters are variables defined in a function declaration
# Arguments - Arguments are the actual values that you pass to the function when you call it



# Prime numbers
def prime(n):
    
    for i in range (2,n+1):
        if(n%i==0):
            print(f"{n} is Not a prime number")
            break
        else:
            print(f"{n} is a prime number")
            
n = int(input("Enter any number : "))
prime(n)

# Passing Function as an Argument
# A function that takes another function as an argument
def fun(func, arg):
    return func(arg) 

def square(x):
    return x ** 2
# Calling fun and passing square function as an argument  
res = fun(square, 5)
print(res)


# Local Variables -  variables which are initialized inside a function and belong only to that particular function
# Global Variables - variables which are defined outside any function and which are accessible throughout the program
# Global Keyword - used inside the function when we need to update the value of the global varibale inside the function
k = 4 # Global Scope
def new():
    global k
    b = 4 # Local Scope
    print(k+b)
    k = k + 5
    print(k)
    k = 6
    print(k)
new()


# Assigning functions to variable
def msg(name):
    return f"Hello, {name}!"

f = msg
print(f("Bharvi"))  


# Storing Fucntions in data structure
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

# Storing functions in a dictionary
d = {
    "add": add,
    "subtract": subtract
}
# Calling functions
print(d["add"](5, 3))       
print(d["subtract"](5, 3)) 


