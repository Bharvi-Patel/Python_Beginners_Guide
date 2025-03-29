# # While - a while loop is used to execute a block of statements repeatedly until a given condition is satisfied.
# # When the condition becomes false, the line immediately after the loop in the program is executed.
# # while expression:
#     # statement(s)

# i = 0
# while(i<10):
#     print(i)
#     i += 1

# # Using else clause with while
# c = 0
# while (c < 6):
#     c += 1
#     print("Heyy")
# else:
#     print("Byeee")


# # For loop - usedd for sequentian traversal
# # In Python, there is “for in” loop which is similar to foreach loop in java
# # for iterator_var in sequence:
# #     statements(s)

# n = int(input("Enter any number : "))
# for i in range(0,n): # same as indexing
#     print(i)

# # with Lists
# l = [20,"kulfi",29,"kasata",27,"popsical"]
# for i in l:
#     print(i)

# # with Tuple
# t = (15,48,65,"solar")
# for i in t:
#     print(i)

# # with String
# s = "Back to December"
# for i in s:
#     print(i)

# # with Dictionary
# d = {"name":"betty","Age":18}
# for i in d:
#     print(i)# only rpints the keys
#     print(i,d[i])#key value pair
# # with set
# set = {21,"rats",56,98,"cats"}
# for i in set:
#     print(i)

# list = ["geeks", "for", "geeks"]
# for index in range(len(list)):# using index of elements in the sequence to iterate
#     print(list[index])


# # Nested Loops - one loop inside another loop
# # or
# #    iterator_var in sequence:
# #    for iterator_var in sequence:
# #        statements(s)
# #    statements(s)

# # or
# #    iterator_var in sequence:
# #    for iterator_var in sequence:
# #        statements(s)
# #    statements(s)

# for i in range(1,5):
#     for j in range(i):
#         print(i, end=" ")
#     print()

# # with else clause
# for i in range(0,4):
#     print(i)
# else:
#     print("Well Done")


# # Loop Control statements - change execution from their normal sequence
# # Continue -  returns the control to the beginning of the loop 
# # skip the current iteratipn and skip to the next
# for letter in 'Look What you Made me do':
#     if letter == 'e' or letter == 'o':
#         continue
#     print('Current Letter :', letter)

# # Break Statement - brings control out of the loop.
# for letter in 'Look What you Made me do':
#     if letter == 'e' or letter == 'o':
#         break
# print('Current Letter :', letter)

# # Pass Statement - to write empty loops
# # Pass is also used for empty control statements, functions and classes.
# for i in range(0,8):
#     pass
# print(i)# prints the last value i.e - 7


# # Multiplication table using for loop
n = int(input("Enter a number : "))

for i in range(1,11):
    m = n*i
    print(m)

i = 1 #multiplication table using while loop
while (i<11):
    print(n*i)
    i+=1


# greet people whose name starts with "B"
l1 = ["Bharvi","Kharva","Bhavyaa"]
for i in l1:
    if(i.startswith("B")):
        print(i)


