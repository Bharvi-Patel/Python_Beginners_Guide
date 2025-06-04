# List Comprehensions - allows us to generate a new list by applying an expression to each item in an existing iterable (such as a list or range)
# j = int(input("Enter number : "))
l1 = [ i for i in range(0,25)]
print(l1)

# 
x = [2,5,8,7,3]
l2 = [i**2 for i in x]
print(l2)

# Syntax
'''
expression for item in iterable if condition
'''

# Conditional statements in list comprehension
l3 = [i for i in x if (i%2==0) ]
print(l3)

# Nested loops in list comprehensions
l4 = [(a,b)for a in range(0,5) for b in range(0,5)]
print(l4)


# List comprehensions with slicing
# Syntax - [expression for item in list[start:stop:step] if condition]
# Return type - list
l5 = [i**2 for i in x [0:3]]
print(l5)

l6 = [i for i in x[0:2] if (i%2==0)]
print(l6)

