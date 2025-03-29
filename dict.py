#lists of key-value pair , dictionary is mutable , cannot contain duplicate values

d = {}# empty dicionary
marks = { "samosa":85,
         "jalebi":99,
         "list":[15,25,"hehehe"]
         }
print(marks)

a = marks["jalebi"]# prints "value" i.e 99
print(a)
b = marks["list"]
print(b)

print(marks.items()) # returns in the form of tuple

print(marks.keys())# returns the keys

print(marks.values())# returns values

marks.update({"jalebi":100,"bhajiya":98})
print(marks)

print(marks.get("shiv"))#returs None if the key doesn't exists in the dictionary
print(marks.get("city", "Not found"))  # Output: Not found
# print(marks["harvi"])# gives error if key doesn't exists

age = marks.pop("list")
print(age)  #removes the key and returns it's value
print(marks) 

my_dict = {"name": "Alice", "age": 25}
last_item = my_dict.popitem()# removes and returns the last key-value pair
print(last_item) 

my_dict.clear()# removes all elements from the dictionary
print(my_dict) 

my_dict = {"name": "Alice", "age": 25}
new_dict = my_dict.copy()
print(new_dict) 

#Create an empty dictionary.Allow 4 friends to enter their fav language as value and use key as their names.Assume that the names are unique
d = {}

name = input("Enter name : ")
lang = input("Enter language : ")
d.update({name:lang})

name = input("Enter name : ")
lang = input("Enter language : ")
d.update({name:lang})

name = input("Enter name : ")
lang = input("Enter language : ")
d.update({name:lang})

name = input("Enter name : ")
lang = input("Enter language : ")
d.update({name:lang})

print(d)

#if keys are same then it will be updated