message = input("Tell me something: ")
print(message)
# When you use the input() function, Python interprets everything the user enters as a string
# % modulo operator - returns remainder

# 7-1
rental_car = input("What kind of rental car would you like? ")
print("Let me see if I can find you a/an " + rental_car.title())

# 7-2
dinner_group = input("How many people are in your group? ")
# Textbook Answer - party_size = int(party_size)
if int(dinner_group) > 8:
    print("Fucking Wait then!")
else:
    print("Go to that table Ahole")

# 7-3
user_number = input("Input a number: ")
if int(user_number) % 10 == 0:
    print("That's multiple of 10!")
else:
    print("not multiple of 10. Fuck off")

# != not equal to

prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program."
# Python must have something(initial value) to check the first time it  reaches the while line
message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)

# flag - set any name as a variable to determine whether or not the entire program is active
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)

# 7-4
toppings = True
while toppings:
    pizza_toppings = input("do you wannna add anything toppings? " + "\nif not type in 'quit'")
    if pizza_toppings != 'quit':
        #pizza_toppings = input("do you wannna add anything toppings? " + "\nif not type in 'quit'") - NameError: name 'pizza_toppings' is not defined
        print(pizza_toppings.title() + " has been added.")
    if pizza_toppings == 'quit':
        print('okay, we are preparing your pizza!')
        break
# Textbook answer
    #else:
        #break

# 7-5
active = True
while active:
    age = input("Enter your age" + "\nOr enter 'quit' ")
    if age == 'quit':
        break
    #elif age == str:
        #print("enter a number")
    elif int(age) <= 3:
        print("Your ticket is free")
    elif int(age) <= 12:
        print("Please pay $10")
    elif int(age) > 12:
        print("Please pay $15")
    # How can I print if input is any string
    #elif type(age) == str: - ValueError: invalid literal for int() with base 10: 'sdgdsg'
    #elif age == str:
    #elif age == 'quit': - this must go to the first because if 'quit' is input it then it cause error cause 'quit' is converted to integer
prompt = "How old are you?"
prompt += "\nEnter 'quit' when you are finished. "
# Textbook answer
while True:
    age = input(prompt)
    if age == 'quit':
        break
    age = int(age)

    if age < 3:
        print("  You get in free!")
    elif age < 13:
        print("  Your ticket is $10.")
    else:
        print("  Your ticket is $15.")

# 7-8
sandwich_orders = ['russian', 'the dude', 'the bomb']
finished_sandwiches = []
while sandwich_orders:
    filled_orders = sandwich_orders.pop()
    print("Making " + filled_orders)
    finished_sandwiches.append(filled_orders)

for finished in finished_sandwiches:
    print(finished + " is done!!")

# 7-9
sandwich_orders = ['pastrami', 'russian', 'pastrami', 'the dude', 'the bomb', 'pastrami']
finished_sandwiches = []
print('Sorry, We are out of pastrami')
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    filled_orders = sandwich_orders.pop()
    print("Making " + filled_orders)
    finished_sandwiches.append(filled_orders)

for finished in finished_sandwiches:
    print(finished + " is done!!")

# 7-10
reponses = {}
active = True

while active:
    name = input("Enter your name: ")
    place = input("If you could visit on place in the world," + "\n Where would you go? ")

    reponses[name] = place

    repeat = input("Does your friend wanna response? Yes/No ")
    if repeat == 'no':
        active = False
        # you don't need to set up 'yes' separately since while is a loop it will continue to run

for names, places in reponses.items():
    print(names + ' would like to go to ' + places)