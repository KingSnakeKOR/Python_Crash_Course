# 9-1
class Restaurant():
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def describe_restaurant(self):
        print(self.name.title() + " serves " + self.type.title())

    def open_restuanrat(self):
        print(self.name.title() + " is now open for business!")

restaurant = Restaurant('the RJs', 'korea contemporary')
restaurant.describe_restaurant()

# 9-2
restaurant1 = Restaurant('jackson', 'italian')
restaurant1.describe_restaurant()

restaurant2 = Restaurant('harbor deli', 'american')
restaurant2.describe_restaurant()

# 9-3
class User():
    def __init__(self, first_name, last_name, age, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender

    def describe_user(self):
        description = "User's name is " + self.first_name.title() + " " + self.last_name.title() \
                      + " , while his/her age is " + str(self.age) + " and it's " + self.gender.title()
        print(description)

    def greet_user(self):
        message = "Welcome " + self.first_name.title() + " " + self.last_name.title() + "!!!"
        print(message)

print("\n")
user1 = User("michael", "jordan", 33, "male")
user1.describe_user()
user1.greet_user()

# 9-4
class Restaurant():
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.number_served = 0

    def describe_restaurant(self):
        print(self.name.title() + " serves " + self.type.title() + "\nWe served " + str(self.number_served) + " people")

    def open_restuanrat(self):
        print(self.name.title() + " is now open for business!")

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, increment_number_served):
        self.number_served = increment_number_served + self.number_served

print("\n")
restaurant = Restaurant('the RJs', 'korea contemporary')
restaurant.describe_restaurant()
restaurant.set_number_served(10)
restaurant.increment_number_served(30)
restaurant.describe_restaurant()

# 9-5
class User():
    def __init__(self, first_name, last_name, age, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.attempts = 0

    def describe_user(self):
        description = "User's name is " + self.first_name.title() + " " + self.last_name.title() \
                      + " , while his/her age is " + str(self.age) + " and it's " + self.gender.title()
        print(description)

    def greet_user(self):
        message = "Welcome " + self.first_name.title() + " " + self.last_name.title() + "!!!"
        print(message)

    def increment_login_attempts(self):
        self.attempts += 1

    def reset_login_attempts(self):
        self.attempts = 0

print("\n")
user1 = User("michael", "jordan", 33, "male")
user1.describe_user()
user1.greet_user()
user1.increment_login_attempts()
user1.increment_login_attempts()
#print(str(user1.attempts())) - not an error but does not print
print(str(user1.attempts))
user1.reset_login_attempts()
print(str(user1.attempts))

# 9-6
class IceCreamStand(Restaurant):
    def __init__(self, name, type):
        super().__init__(name, type)
        self.flavors = " "

    def flavor(self, flavors):
        self.flavors = flavors

    def desciption_flavor(self):
        description = "My favorite flavor is " + self.flavors
        print(description)

icecreamstand = IceCreamStand("HOHO", "French")
icecreamstand.flavor("strawberry")
icecreamstand.desciption_flavor()

#to store a list of items (Text Book Answer)
class IceCreamStand(Restaurant):
    def __init__(self, name, type="Icecream"):
        super().__init__(name, type)
        self.flavors = []

    def flavor(self):
        print("my favorite flavor is ")
        for flavor in self.flavors:
            print(flavor)

icecreamstand = IceCreamStand("HOHO")
# myflavors = ["strawbeery", "kiwi", "blueberry"] - this is wrong
# icecreamstand.flavor = ["strawbeery", "kiwi", "blueberry"] - flavor must be the same as attributes which flavors
icecreamstand.flavors = ["strawbeery", "kiwi", "blueberry"]
icecreamstand.flavor()

# 9-7
class Admin(User):
    def __init__(self, first_name = "kim", last_name = "ryan", age = 19, gender = "male"):
        super().__init__(first_name, last_name, age, gender)
        self.privileges = []

    def show_privileges(self):
        print("Here are admin privileges: ")
        for privilege in self.privileges:
            print(privilege)

admintest1 = Admin()
admintest1.privileges = ["can delete post", "can ban user", "can add post"]
admintest1.show_privileges()

# 9-8
class Admin(User):
    def __init__(self, first_name = "kim", last_name = "ryan", age = 19, gender = "male"):
        super().__init__(first_name, last_name, age, gender)
        self.privileges = Privileges()

class Privileges():
    def __init__(self):
        self.privileges = []

    def show_privileges(self):
        print("Here are admin privileges: ")
        for privilege in self.privileges:
            print(privilege)

testest1 = Admin()
testest1.describe_user()

testest1.privileges.show_privileges()
testest1.privileges.privileges = ["can delete post", "can ban user", "can add post"]
testest1.privileges.show_privileges()

# 9-9
class Car():
    """A simple attempt to represent a car."""

    def __init__(self, manufacturer, model, year):
        """Initialize attributes to describe a car."""
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.manufacturer + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles


class Battery():
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=60):
        """Initialize the batteery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 60:
            range = 140
        elif self.battery_size == 85:
            range = 185

        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

    def upgrade_battery(self):
        self.battery_size = 85


class ElectricCar(Car):
    """Models aspects of a car, specific to electric vehicles."""

    def __init__(self, manufacturer, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(manufacturer, model, year)
        self.battery = Battery()


mycar_test1 = ElectricCar("honda", "civic", 2019)
mycar_test1.battery.describe_battery()
mycar_test1.battery.get_range()
mycar_test1.battery.upgrade_battery()
mycar_test1.battery.describe_battery()
mycar_test1.battery.get_range()

# 9-13
from collections import OrderedDict

python_words = OrderedDict()

python_words = {'for':'loop',
                'if':'conditional',
                'list':'collection',
                'dict':'key-value',
                'python':'conquer'
                }
for word in python_words.keys():
    print("In python " + "'" + word + "'" + " stands for " + python_words[word])

for word, meanings in python_words.items():
    print(word.title() + " : " + meanings.title())

# 9-14
from random import randint

class Dice():
    def __init__(self, sides=6):
        self.sides = sides
        print(str(sides))

    def roll_die(self):
        x = randint(1, 6)
        self.sides = x
        print(str(self.sides))

testest1 = Dice()
testest1.roll_die()
testest1.roll_die()

#Textbook answer
class Dice():
    def __init__(self, sides = 6):
        self.sides = sides

    def roll_dice(self):
        return randint(1, self.sides)

d6 = Dice()
result = []
for xyz in range(1,11):
    hello = d6.roll_dice()
    result.append(hello)
print(result)

d10 = Dice(sides=10)
result = []

for xyz in range(1,11):
    hello = d10.roll_dice()
    result.append(hello)
print(result)

# 9-6 Review - Far better code

class Restaurant():
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.number_served = 0

    def describe_restaurant(self):
        print(self.name.title() + " serves " + self.type.title() + "\nWe served " + str(self.number_served) + " people")

    def open_restaurant(self):
        print(self.name.title() + " is now open for business!")

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, increment_number_served):
        self.number_served = increment_number_served + self.number_served

class IceCreamStand(Restaurant):
    def __init__(self, name, type):
        super().__init__(name, type)
        self.list_flavors = []

    """
    I wanted to include multiple input of flavors(arbitrary number of arguments) 
    that could be stored in a list so basically converted tuple to list
    """
    def flavor1(self, *flavors):
        self.flavors = flavors
        for flavor in self.flavors:
           self.list_flavors.append(flavor)
        print(self.list_flavors)

    def show_flavor(self):
        print("my favorite flavors are: ")
        for flavor in self.list_flavors:
            print("- " + flavor)

icecreamstand = IceCreamStand("tomntoms", "icecream")
icecreamstand.describe_restaurant()
icecreamstand.flavor1('apple', 'honey')
icecreamstand.show_flavor()

