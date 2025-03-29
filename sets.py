#set is a collection of well-defined objects
#non-repeative , unordered , unindexed ,  no way to change items in sets

s1 = set()
print(s1)# not in order

s2 = {12,56,2,5,6}
s3 = {56,45,"dogs"}
t = type(s2)
print(t)

#set methods
s2.add(4568)
print(s2)

s2.remove(2)#  Removes an element; raises an error if the element is not found.
print(s2)

s3.discard(5)#  Removes an element without error if it does not exist.
print(s3)

element = s2.pop()# Removes and returns an arbitrary element.
print(element) 

s3.clear()# Removes all elements from the set.
print(s3)

s = {1,2,5,4,6,8}
print(len(s))

print(s.union({12,5}))
print(s.union(s2))

print(s.intersection({12,5}))
print(s.intersection(s2))

s4 = {20,20.0,"20"}
print(len(s4))# because 1=1.0 python values dekhta hai agar same hai toh interpreter ko datatype se farak nahi padta


