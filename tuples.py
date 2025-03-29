# tuples are immutable
t1 = (45,2,3,"star","Moon",13,"Midnights") 
print(t1)
t2 = (1,)
print(type(t2))

#tuple methods
x = t1.count(3)
print(x)

i = t1.index("Moon")
print(i)

repeat = t2 * 3
print(repeat)

y = t1 + t2
print(y)

v = t1[2:5]
print(v)


