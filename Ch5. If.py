cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

#Testing for equality is case sensitive in Python
# Multiple conditions 'and' and 'or'

# 5-3
alien_color = ['green', 'yellow', 'red']
# if color in alien_color == 'green': - NameError: name 'color' is not defined
for color in alien_color:
    if color == 'green':
        print('You just earned 5 points!')
# Textbook answer
alien_color = 'green'
if alien_color == 'green':
    print('You just earned 5 points!!!')

# 5-4
alien_color = ['green', 'yellow', 'red']
for color in alien_color:
    if color == 'green':
        print('You just earned 5 points~!')
    else:
        print('You just earned 10 points')

# 5-5
alien_color = ['green', 'yellow', 'red']
for color in alien_color:
    if color == 'green':
        print('You just earned 5 points~~!')
    elif color == 'yellow':
        print('You just earned 10 points')
    else:
        print('You just earned 15 points')
    #else color == 'red': - you can't do this cause nothing can come after else!!!

# 5-6
#age = '32' - this reads as string
age = 32
if age < 2:
    print('you are a baby')
elif age < 4:
    print('you are a toddler')
elif age < 13:
    print('you are a kid')
elif age < 20:
    print('you are a teenager')
elif age < 65:
    print('you are an adult')
else:
    print('you are an elder')

# 5-7
favorite_fruits = ['apple', 'clementine', 'blackberry']
for fruit in favorite_fruits:
    if fruit == 'apple':
        print('You really like', fruit)
    if fruit == 'clementine':
        print('You really like', fruit)
    if fruit == 'blackberry':
        print('You really like', fruit)

#Checking that a list is not empty pg 91
requested_toppings = []
if requested_toppings:
# When the name of a list is used in an if statement, Python returns True if the list contains at least one item; an empty list evaluates to False.
    for requested_topping in requested_toppings:
        print("adding" + requested_topping + '.')
    print("\nfinished making your pizza!")
else:
    print("are you sure you want a plain pizza?")

# 5-8
usernames = ['admin', 'happy07', 'dogmama', 'user', 'genius']
for username in usernames:
    if username == 'admin':
        print('Hello', username, ", would you like to see a status report?")
    else:
        print('Hello', username, "welcome")

# 5-9
users = []
if users:
    for user in users:
        print("we got some users")
else:
    print('we need to find some users!')

# 5-10
current_users = ['Mike', 'green', 'Sexy', 'happy', 'strong']
new_users = ['rich', 'charisma', 'sexy', 'Loved', 'strong']

#for users in current_users: - this is upside down this is checking current usersname in new username it should be vice versa
    #if users.lower() == new_users: - need to use 'in' to find whether a particular value is already in the list
    #if users.lower() in new_users.lower(): - AttributeError: 'list' object has no attribute 'lower'
#current = [for current.lower() in current_users] - SyntaxError: invalid syntax
#current = list(for current1 in current_users) - SyntaxError: invalid syntax

current = [current.lower() for current in current_users]

for users in new_users:
    if users.lower() in current:
        print(users, 'already taken. Try others')
    else:
        print(users, 'that user name is available')

# 5-11
# numbers = [int(range(1,10))] - TypeError: int() argument must be a string, a bytes-like object or a number, not 'range'
numbers = list(range(1,10))
for number in numbers:
    if number == 1:
        print(str(number) + "st")
    if number == 2:
        print(str(number) + "nd")
    if number == 3:
        print(str(number) + "rd")
    #elif number > 3: - TypeError: '>' not supported between instances of 'range' and 'int'
    elif number > 3:
        print(str(number) + "th")
