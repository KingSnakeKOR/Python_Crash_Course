file_path = 'C:/Users/admin\Desktop\파이썬\ehmatthes-pcc-v1.0.0-12-gf555082\ehmatthes-pcc-f555082\chapter_10\pi_million_digits.txt'

with open(file_path) as file_object:
    contents = file_object.read()
    print(contents[:400])
    #lines = file_object.readline() - this only reads the first line! No S
    lines = file_object.readlines()

with open(file_path) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string[:53] + "......")
print(len(pi_string))

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi ")
else:
    print("Your birthday does not appear")

x = "3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"
print(len(x))

file_path2 = 'C:/Users/admin\Desktop\파이썬\ehmatthes-pcc-v1.0.0-12-gf555082\ehmatthes-pcc-f555082\chapter_10\pi_digits.txt'
with open(file_path2) as file_object2:
    for line1 in file_object2:
        print(line1.strip())

# 10-1
"""read entire file"""
with open('learning_python.txt') as practice_object:
    readthis = practice_object.read()
    print(readthis)

"""lopping over the file object"""
with open('learning_python.txt') as practice_object:
    print("\n")
    for line4 in practice_object:
        print(line4.strip())

"""storing the line in the list and then workign with them outside the with block"""
with open('learning_python.txt') as practice_object:
    outsides = practice_object.readlines()
print("\n")
for outside in outsides:
    print(outside.strip())

# 10-2
with open('learning_python.txt') as practice_object:
    outsides = practice_object.readlines()
print("\n")
xyz = 'python'
for outside in outsides:
    if xyz.title() in outside:
        print(outside.replace(xyz.title(), 'C'))

# Textbook Answer
for outside in outsides:
    print(outside.replace(xyz.title(), 'C'))

#for outside in outsides:
    #if xyz.title() in outside:
        #outside.replace(xyz.title(), 'C')
        #print(outside)
    #else:
        #print("none")

# 10-3
user_name = input("What is your name? ")

filename = 'guest.txt'
with open(filename, 'a') as guest_file:
    guest_file.write(user_name)

# 10-4
filename1 = "guest_book.txt"
active = True
while active:
    name = input("What is your name? (if you don't want to respond type'q') ")
    if name != "q":
        print("Welcome, " + name.title())
        with open(filename1, 'a') as recordings:
            recordings.write(name + "\n")
    else:
        active = False

# 10-5
reasons = "programming_reasons.txt"
active1 = True
while active1:
    reasoning = input("Why do you like programming? type 'q' to quit ")
    if reasoning != 'q':
        with open(reasons, 'a') as reason_file:
            reason_file.write(reasoning + "\n")
    else:
        active1 = False

# Testbook Answer
while True:
    response = input("\nWhy do you like programming? ")
    responses.append(response)

    continue_poll = input("Would you like to let someone else respond? (y/n) ")
    if continue_poll != 'y':
        break

with open(reasons, 'a') as f:
    for response in responses:
        f.write(response + "\n")

# 10-6
number1 = input("Enter a number: ")
number2 = input("Enter a second number: ")
try:
    hello = int(number1) + int(number2)
except ValueError:
    print("can't divide something by 0")
else:
    print("The added number is " + str(hello))

# 10-7
while True:
    number1 = input("Enter a number: ")
    if number1 == 'q':
        break
    number2 = input("Enter a second number: ")
    if number2 == 'q':
        break
    try:
        hello = int(number1) + int(number2)
    except ValueError:
            print("Error! enter a number please")
    else:
        print("The added number is " + str(hello))

# 10-8
file_path3 = ["C:/Users/admin\PycharmProjects\Python_Crash_Course/dogs.txt",
              "C:/Users/admin\PycharmProjects\Python_Crash_Course/cats.txt"]
for files in file_path3:
    try:
        with open(files) as dog_names:
            ggg = dog_names.read()
            print(ggg)
    except FileNotFoundError:
        print('File have not been found')

# 10-9
file_path3 = ["C:/Users/admin\PycharmProjects\Python_Crash_Course/dogs.txt",
              "C:/Users/admin\PycharmProjects\Python_Crash_Course/cats.txt"]
for files in file_path3:
    try:
        with open(files) as dog_names:
            ggg = dog_names.read()
            print(ggg)
    except FileNotFoundError:
        pass

# 10-10
gutenberg_path = "C:/Users/admin\PycharmProjects\Python_Crash_Course/pride_and_prejudice.txt"

try:
    with open(gutenberg_path, encoding='utf-8') as gutenberg:
    #with open(gutenberg_path) as gutenberg:
        pp = gutenberg.read()
except FileNotFoundError:
    print("file have not been found")
else:
    #pp.lower.count('the')
    xxx = pp.lower().count('the')
    print(xxx)

## practice
import json

numbers = [2, 36, 44, 52, 69, 17]
filenamee = 'numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)

filenamee = 'numbers.json'
with open(filenamee) as f_obj:
    numbers = json.load(f_obj)

print(numbers)

# 10 -11
favorite_number = input('What is your favorite number?')
favorite_number1 = 'favorite_number.json'
with open(favorite_number1, 'w') as f_obj2:
    json.dump(favorite_number, f_obj2)

favorite_number1 = 'favorite_number.json'
with open(favorite_number1) as f_obj2:
    #json.load(favorite_number1) - AttributeError: 'str' object has no attribute 'read'
    xyy = json.load(f_obj2)
    # print("I know your favorite number! It's " + xyy)
    print("I know your favorite number! It's " + str(xyy))

# 10-12
favorite_number1 = 'favorite_number.json'
try:
    with open(favorite_number1) as f_obj2:
        xyy = json.load(f_obj2)
except FileNotFoundError:
    print("File does not exist")
    favorite_number = input('What is your favorite number?')
    favorite_number1 = 'favorite_number.json'
    with open(favorite_number1, 'w') as f_obj2:
        json.dump(favorite_number, f_obj2)
else:
    print("I know your favorite number! It's " + str(xyy))

# 10-3
def get_stored_username():
    """Get stored username if available."""
    filename = 'username.json'
    try:
        with open(filename) as f_objj:
            username = json.load(f_objj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name?? ")
    filename = 'username.json'
    with open(filename, 'w') as f_objj:
        json.dump(username, f_objj)
        print("We'll remember you when you comeback, " + username + "!")
    return username

def greet_user():
    filename = 'username.json'
    try:
        with open(filename) as f_objj:
            username = json.load(f_objj)
    except FileNotFoundError:
        username = input("What is your name? ")
        with open(filename, 'w') as f_objj:
            json.dump(username, f_objj)
            print("We'll remember you when you comeback, " + username + "!")
    else:
        correct_username = input("what is your username? ")
        if username != correct_username:
            print("We don't have your information")
            get_new_username()
        else:
            print("Welcome back, " + username + "!")

greet_user()