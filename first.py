#First program

print("Hello,World!")

print("Twinkle Twinkle Little star,"
"How i wonder what you are")

# import pyjokes
# joke = pyjokes.get_joke()
# print(joke)

# REPL - Read Evaluate Print Loop : write Python on the terminal,enter,it will work as a calculator!!!
'''python interpreter humse python code leke use machine code mein convert karta hai 
   Python was created by Guido van Rossum'''
# PyTTSX3 is a  module used for text to speech
import pyttsx3
engine = pyttsx3.init()
engine.say("Come Party with The Bhoothnath, Relax man!")
engine.runAndWait()


import os
directory_path = '/'
contents = os.listdir(directory_path)
for item in contents:
    print(item)


# escape characters
x = "you belong" \
" with me"

'''
    \n = new line
    \t = tab space
    \    
'''

y = "nasjcjh dsvnsdjn  jvhw \"dsdss\" "
