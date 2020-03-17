magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

# 4-1
print("\n")
pizzas = ['페페로니', 'tomato chicken', 'potato gold']
for pizza in pizzas:
    print(pizza)
for pizza in pizzas:
    print("I love", pizza, "pizza")
print("I really love pizza!!!")

# 4-3
# numbers1 = [for number1 in range(1, 21)] - SyntaxError: invalid syntax
# numbers1 = for number in range(1, 21) - SyntaxError: invalid syntax
for number in range(1, 21):
    print(number)
# Textbook answer
numbers1 = list(range(1,21))
for number in numbers1:
    print(number)

# 4-5
million = list(range(1, 1000001))
print(max(million))
print(min(million))
print(sum(million))

# 4-7
# threes = list(three for three in range(1,31,3)) - this is NOT an error; but it prints the list not individual value of the list
#print(threes)
# Textbook answer
threes = list(range(1,31,3))
for three in threes:
    print(three)

# 4-8
# cubes = list(cube for cube in range(1,11)) -TypeError: unsupported operand type(s) for ** or pow(): 'list' and 'int'
# print(cubes**3)
cubes = list(range(1,11))
for cube in cubes:
    print(cube**3)

# 4-9
list_cubes = [cube**3 for cube in range(1,11)]
print(list_cubes)
# Texbook answer
for cube1 in list_cubes:
    print(cube1)

players = ['charles', 'michael', 'martina', 'florence', 'eli']
print(players[-3:])
print(players[:-3])
print(players[1:-1])

for player in players:
    print(player.title())

#copying a List - basically creating an entirely separate list
my_foods = ['pizza', 'cheese', 'carrot']
friends_food = my_foods[:]

# my_foods = friends_food basically points to the same list with two variable

# 4-11
my_pizzas = ['페페로니', 'tomato chicken', 'potato gold']
friends_pizzas = my_pizzas[:]

my_pizzas.append('shrimp')
friends_pizzas.append('cheese')

print('My favrotie pizzas are: ', my_pizzas)
print("My friend's  favorite pizzas are: ", friends_pizzas)
# Textbook answer
print('\nMy favorite pizzas are: ')
for pizza in my_pizzas:
    print("-", pizza)
print('\nMy friends favorite pizzas are: ')
for pizzaa in friends_pizzas:
    print("-", pizzaa)

# 4 - 13
basic_foods = ('french fries', 'onion rings', 'kimchi', 'smoked beans', 'ramen')
for food in basic_foods:
    print(food)

basic_foods = ('rice', 'pepper', 'kimchi', 'smoked beans', 'ramen')
for food in basic_foods:
    print(food)
    