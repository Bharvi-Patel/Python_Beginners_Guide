# Lists are containers used to store multiple values of any data types , lists are mutable
L1 = [20,29,27,"Ice-Cream","Gulab Jamun","sheera",25.36]
print(L1)

print(L1[3])
 
L1[2] = "howw" #replaces 2  index's value with howw 
print(L1)

print(L1[0:4])

L1.append("Idli") #at the end of the list
L1.insert(7,"Dosa")
print(L1)

L2 = [23,5,24,12,78,99,56,22.5,1.2]
L2.sort() # sort the numreic list
print(L2)

L1.reverse()
print(L1)

L1. pop(6) #removes at paticular index ,deleted item ko print bhi karta hai
print(L1)

L2.remove(78)
print(L2)


# ask user the name of the 7 fruits and enter it in the list
L3 = []
f1 = input("Enter fruit name : ")
L3.append(f1)

f2 = input("Enter fruit name : ")
L3.append(f2)

f3 = input("Enter fruit name : ")
L3.append(f3)

f4 = input("Enter fruit name : ")
L3.append(f4)

f5 = input("Enter fruit name : ")
L3.append(f5)

f6 = input("Enter fruit name : ")
L3.append(f6)

f7 = input("Enter fruit name : ")
L3.append(f7)

print(L3)