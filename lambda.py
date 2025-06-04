# Lambda - anonymous functions , function is without a name

str = "Who Let the DOgs Out"
str1 = lambda fn : fn.upper()
print(str1(str))

# lambda with conditions
n = lambda x :"Positive" if (x>0) else "Negative" if (x<0) else "Zero"
print(f"Number is {n(-4)}")
print(f"Number is {n(0)}")
print(f"Number is {n(5)}")

# Lambda with List Comprehension
li = [lambda arg=x: arg * 10 for x in range(1, 5)]
for i in li:
    print(i())

# Lambda with multiple statements
calc = lambda x, y: (x + y, x * y)
res = calc(3, 4)
print(res)  


# lambda with filter() function -  takes in a function and a list as arguments ,
#  it's a way to way to filter out all the elements of a sequence “sequence”, for which the function returns True.
m = [29,54,3,6,8]
s = filter(lambda x : (x%2==0),m)
print(list(s))

# Lambda with map() - takes in a function and a list as an argument
# The function is called with a lambda function and a new list is returned which contains all the lambda-mmodified items returned by that function for each item.
t = map(lambda x: x*3,m)
print(list(t))

# Lambda with reduce() - takes in a function and a list as an argument
# The function is called with a lambda function and an iterable and a new reduced result is returned,This performs a repetitive operation over the pairs of the iterable.
from functools import reduce
a = [1, 2, 3, 4]
b = reduce(lambda x, y: x * y, a)
print(b)  


