p = 58-21
print(p)

# Arithmetic Operators
a = 15
b = 4

# Addition
print("Addition:", a + b)  

# Subtraction
print("Subtraction:", a - b) 

# Multiplication
print("Multiplication:", a * b)  

# Division
print("Division:", a / b) 

# Floor Division
print("Floor Division:", a // b)  

# Modulus
print("Modulus:", a % b) 

# Exponentiation
print("Exponentiation:", a ** b)  

# Comparison Operators - returns either true or false
c = 13
d = 33

print(c > d)
print(c < d)
print(c == d)
print(c != d)
print(c >= d)
print(c <= d)

# Logical Operators
e = True
f = False
print(e and f) #Logical AND
print(e or f) #Logical OR
print(not e) #Logical NOT


#BItwise Operators
g = 10
h = 4

print(g & h)
print(g | h)
print(~g)
print(g ^ h)
print(g >> 2)
print(g << 2)

#Assignment Operators 
i = 10
j = i
print(j)
j += i
print(j)
j -= i
print(j)
j *= i
print(j)
j <<= i
print(j)

# Identity Operators 
# In Python, is and is not are the identity operators both are used to check if two values are located on the same part of the memory. 
# Two variables that are equal do not imply that they are identical. 

# is          True if the operands are identical 
# is not      True if the operands are not identical 


k = 10
l = 20
m = k

print(k is not l)
print(k is m)

# Membership Operators 
# In Python, in and not in are the membership operators that are used to test whether a value or variable is in a sequence.

# in            True if value is found in the sequence
# not in        True if value is not found in the sequence

x = 24
y = 20
list = [10, 20, 30, 40, 50]

if (x not in list):
    print("x is NOT present in given list")
else:
    print("x is present in given list")

if (y in list):
    print("y is present in given list")
else:
    print("y is NOT present in given list")


# Ternary Operator
# in Python, Ternary operators also known as conditional expressions are operators that evaluate something based on a condition being true or false.

# Syntax :  [on_true] if [expression] else [on_false] 

r, s = 10, 20
min = r if r < s else s

print(min)



