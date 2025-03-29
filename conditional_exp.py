# if - executes a block of code if the given condition is true.
age = 20

if age >= 18:
    print("Eligible to vote.")
           #  or
age = 19
if age > 18: print("Eligible to Vote.")

# if-else - Else allows us to specify a block of code that will execute if the condition(s) associated with an if or elif statement
#  evaluates to False. Else block provides a way to handle all other cases that don't meet the specified conditions.
Age = 10

if Age <= 12:
    print("Travel for free.")
else:
    print("Pay for ticket.")
            # or
marks = 45
res = "Pass" if marks >= 40 else "Fail"

print(f"Result: {res}")

# elif statement - stands for "else if." 
# It allows us to check multiple conditions , providing a way to execute different blocks of code based on which condition is true.
aGe = 25

if aGe <= 12:
    print("Child.")
elif aGe <= 19:
    print("Teenager.")
elif aGe <= 35:
    print("Young adult.")
else:
    print("Adult.")


# Nested if..else means an if-else statement inside another if statement. We can use nested if statements to check conditions within conditions.
agE = 70
is_member = True

if agE >= 60:
    if is_member:
        print("30% senior discount!")
    else:
        print("20% senior discount.")
else:
    print("Not eligible for a senior discount.")


# A ternary conditional statement is a compact way to write an if-else condition in a single line.
#  It’s sometimes called a "conditional expression."
# Assign a value based on a condition
New_age = 20
s = "Adult" if New_age >= 18 else "Minor"

print(s)


# match-case statement is Python's version of a switch-case found in other languages.
#  It allows us to match a variable's value against a set of patterns.
number = 6

match number:
    case 1:
        print("One")
    case 2 | 3:
        print("Two or Three")
    case _:
        print("Other number")


# Find greatest of four numbers enterend by user
n1 = int(input("Enter a number : "))
n2 = int(input("Enter a number : "))
n3 = int(input("Enter a number : "))
n4 = int(input("Enter a number : "))

if(n1>n2 and n1>n3 and n1>n4):
    print(F"{n1} is the greatest!")
elif(n2>n1 and n2>n3 and n2>n4):
    print(f"{n2} is the greatest!")
elif(n3>n1 and n3>n2 and n3>n4):
    print(f"{n3} is the greatest!")
else:
    print(f"{n4} is the greatest!")


# find out whether  student is pass or fail,if it requires total 40% and at least 33% in each subject to pass.
# Assume 3 subjects and take marksa as an input from the user
s1 = int(input("Enter marks : "))
s2 = int(input("Enter marks : "))
s3 = int(input("Enter marks : "))

total_percentage = ((100)*(s1+s2+s3))/300

if(total_percentage>=40 and s1>=33 and s2>=33 and s3>=33):
    print("you passed the exam : ", total_percentage)
else:
    print("You failed!")


# Membership keyword
