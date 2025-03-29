# Strings : sequence of characters,string is immutable
name = "Bharvi"

print(len(name))

# String slicing : indexing is from 0 (for left to right) and it's from -1(for reverse
# S =  name[ind_start:ind_end]
str1 = name[0:4] #0 to 3 (4 won't be included)
print(str1)
char = name[2]
print(char)
str2 = name[1:]
print(str2)
str5 = name[:3]
print(str5)
str3 = name[:]
print(str3)

#  negative slicing
surname = "Patel"
str4 = surname[-4:-1] #char at -1 won't be included
print(str4)


# Slicing with skip value
# s = name[start_index:end_index:skip_value]

song = "We are Never Ever Getting Back Together"
s1 = song[1:29:3]#skips 2 and prints the third value
print(s1)
s2 = song[1: :4]
print(s2)
s3 = song[: : ]
print(s3)
s4 = song[0:30: ]
print(s4)
print(song[::-1])


print(name.endswith("vi"))
print(song.startswith("bh"))
print(surname.capitalize())

del surname
s6 = "sparks fly"
s7 = s6.replace("fly", ",glitter, is our wolrd!")
print(s6)
print(s7)

s8 = "Hello World"
print(s8.upper()) # output: HELLO WORLD
print(s8.lower()) #hello world

s9 = "   Long Live      "
# Removes spaces from both ends
print(s9.strip())    


#display user entered name followed by Good Afternoon
s10 = input("Enter anything : ")
s11 = s10 + "Good Afternoon"
print(s11)

#replace name and date in letter template
letter = '''Dear <|Name|>,
            you are selected!
            <|Date|>'''
print(letter.replace("<|Name|>","Bharvi").replace("<|Date|>","20 October 2025"))

#find double space
s12 = "Down  Bad "
print(s12.find("  ")) #returns index

print(s12.replace("  ","   "))
