# Recursion - A function calls itself
#  a function calling itself directly or indirectly to solve a problem by breaking it down into simpler and more manageable parts

n = int(input("Enter a number : "))
def fact(n):
    if (n==0 or n==1): # Base Case
        return 1        
    
    return n*fact(n-1) # Recursive Case
    
print(f"Factorial of {n} is {fact(n)}")


# *args - accept an arbitrary number of arguments
# **kargs - key-value pair arguments

def fun(*args):
    return args
print(fun(1, "princess", 3, 4)) 
print(fun(5, 10, 15))   

def fun(**kwargs):
    for k, val in kwargs.items():
        print(k, val)

fun(a=1, b="Mango", c=3)


# Calculate the sum of first n natural numbers
n = int(input("Enter a number : "))
def sum(n):
    if(n==0):
        return 0
    return n + sum(n-1)
print(f"Sum of first {n} natural numbers are : {sum(n)} ")

# print all elements of list in sequence(use indx and list as parameters)
def print_list(list,idx=0):
    if(idx == len(list)):
        return 
    print(list[idx])
    print_list(list,idx+1)

songs = ["Teardrops on my guitar", "White Horse", "Long Live", "All Too Well", "Clean", "New Years Day", "Archer", "My Tears Ricochet", "Dorthea", "Midnight Rain", "The Alchemy"]
print_list(songs)