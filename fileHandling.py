# # File I/O : File Input and Output : to perform operations on a file using Python.

# f = open("demoForFile.txt","r") 
# info = f.read
# print(info)
# print(type(info))
# f.close()

# ''' combine bhi kar sakte e.g rt
# MODES -
# r        : open for reading(default)
# w        : open for writing,truncatinf the file first
# x        : create a new file and opem it for writing
# a        : open for writing,appending to the end of the file if it exists
# b        : binary mode
# t        : text mode(default)
# +        : open a disk file for updating(reaidn & writing)
# '''

# # read(25) - prints only first 5 letters
# # readline() - read one line at a time(read until the end of line) 
# # readlines() - prints entire file
# # readable()


# # Writing onto the file
# f1 = open("demoForFile.txt","w")
# f1.write("We are never ever ever getting back together")
# f1.close()


# # append 
# f2 = open("demoForFile.txt","a")
# f2.write("\nyou go talk to your friends talk to my friends talk to me")
# f2.close()


# # with syntax
# with open("demoForFile.txt","a") as f3:
#     data = f3.read() 
#     print(data)
# with automatically close kar deta hai file ko


# # Deleting a file using os module
# import os
# os.remove("sample.txt") # file is deleted even from the storage


# Replace all occurrences of "Java" with "Python" in the practice.txt file
with open("practice.txt","r") as f4:
    data = f4.read()

new_data = data.replace("Java","Python")
print(new_data)

with open("practice.txt","w") as f4:
    f4.write(new_data)


# Search if the word "learning" exists in the file or not
word = "learning"
with open("practice.txt","r") as f5:
    data = f5.read()
    if(data.find(word) != -1):
        print("Found!!!")
    else:
        print("Not Found!!!")


# Find in which line of the file does the word "learning" occur first. Print -1 if the word not found.
def check_for_line():
    word = "learning"
    data = True
    line_no = 1
    with open("practice.txt","r") as f5:
        while data:
            data = f5.readline()
            if(word in data):
                print(line_no)
                return
            line_no += 1

    return -1

check_for_line()



# From a file containing numbers seperated by comma,print the count of even numbers.
count = 0
with open("practice2.txt","r") as f6:
    data = f6.read()
    print(data)

    nums = data.split(",")
    for i in nums:
        if(int(i) % 2 == 0):
            count += 1
print(count)