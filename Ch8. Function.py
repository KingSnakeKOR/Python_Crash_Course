# 8-1
def display_meesage():
    """First practice"""
    print("I'm learning about Python Function this chapter!")

display_meesage()

# 8-2
def favorite_book(book_title):
    """printing favorite book"""
    print("My favorite book is " + book_title.title() + "!!")

favorite_book('시련은 있어도 실패는 없다')

# 8-3
def make_shirt(size, text):
    """making shirt with size and printed text"""
    print("You ordered size " + size.title() + " that says " + "'" + text.title() + "'")
# you must put in quotes I guess the default is string type
make_shirt('m', "I love food")
make_shirt(text = 'i love hip hop' ,size='xl')
# order of argument does not matter for keyword argruments

# 8-4
def make_shirt(size = 'l', text = 'i love python'):
    """making shirt with size and printed text"""
    print("You ordered size " + size.title() + " that says " + "'" + text.title() + "'")

make_shirt()
make_shirt('m')
make_shirt('s',"what's up")

# 8-5
def describe_city(name_city, country = 'USA'):
    """describe a city and country"""
    print(name_city.title() + " is in " + country.title())

describe_city('new york')
#describe_city(new york) - SyntaxError: invalid syntax - must have quotes
describe_city('seoul', 's.korea')
describe_city('tokyo', country = "japan")

# 8-6
def city_country(city, country):
    """Just list city and country"""
    city_country = city.title() + ", " + country.title()
    return city_country

example1 = city_country("seoul", "s.korea")
print(example1)
example2 = city_country("new york", "united states")
print(example2)

# 8-7
def make_album(artist_name, album_title):
    "Make a Dict with function"
    album_info = {"Artist Name":artist_name, "Album Title":album_title}
    return album_info

example1 = make_album("psy", "gangnam style")
print(example1)
example2 = make_album("beatles", "let it be")
print(example2)

def make_album(artist_name, album_title, num_track = ""):
    "Make a Dict with function"
    album_info = {"Artist Name":artist_name, "Album Title":album_title}
    if num_track:
        album_info['Number of Tracks'] = num_track
    return album_info

example1 = make_album("hello", "title", "50")
print(example1)
example2 = make_album("hi", "test")
print(example2)

# 8-8
def make_album(artist_name, album_title, num_track = ""):
    "Make a Dict with function"
    album_info = {"Artist Name":artist_name, "Album Title":album_title}
    if num_track:
        album_info['Number of Tracks'] = num_track
    return album_info

while True:
    print("Please input the following:")
    print("(type 'q' if you don't want to)")
    name = input("Favorite Artist: ")
    if name == "q":
        break
    title = input("The Album title of your favorite artist: ")
    if title == "q":
        break
    example1 = make_album(name, title)
    print(example1)
    # Textbook에서는 track을 안 넣었는 데 만약 넣으면 어떻게 하지?
    #tracks = input("List the number of tracks: ")
    #if title == "q":

print("thanks for responding!")

# 8-9
magician_names = ['emulsion', 'mr.nice', 'dreamer']
modified_names = []

def show_magicians(magician_names):
    for magician_name in magician_names:
        print("This magician name is " + magician_name.title())

show_magicians(magician_names)


# 8-10
# Textbook answer
def make_great(magician_names):
    while magician_names:
        magician_name = magician_names.pop()
        modified_name = magician_name + " the Great"
        modified_names.append(modified_name)

    for name in modified_names:
        magician_names.append(name)

    #MUST add return to copy the list not modify it
    return magician_names

make_great(magician_names)
show_magicians(magician_names)


    # Error - pop from an empty list
    #while magician_names:
        #magician_name = magician_names.pop()
        #magician_names.append(magician_names.pop() + "the Great")
#print(make_great(magician_names))
    #for magician_name in magician_names:
        #magiciain_names[magician_name] = magiciain_name + "the Great" - TypeError: list indices must be integers or slices, not str
        #magician_names[] = magician_name + "the Great" - SyntaxError: invalid syntax

# 8-11
great_magicians = make_great(magician_names[:])
show_magicians(great_magicians)
print('skipped')
show_magicians(magician_names)

# 8-12
def sandwiches_list(*ingredients):
    print("Here are the ingredients for your sandwich: ")
    for ingredient in ingredients:
        print("- " + ingredient)
    print("Would you like to add anything else?")

sandwiches_list("ham", "cheese", "egg", "whesat", "cajun majo")

# 8-13
def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

example_profile = build_profile('Michael', 'Jordan', location = "charlotte", worth = "billionaire", charisma = "sick")

# 8-14
def cars(manufacturer, model, **cars_info):
    car_profile = {}
    car_profile["manufacturers"] = manufacturer
    car_profile["models"] = model
    for key, value in cars_info.items():
        car_profile[key] = value
    return car_profile

testing_cars = cars("hyundai", "santa fe", year = "2019", safety_grade = "100")
print(testing_cars)

# Textbook answer
def make_car(manufacturer, model, **options):
    """Make a dictionary representing a car."""
    car_dict = {
        'manufacturer': manufacturer.title(),
        'model': model.title(),
        }
    for option, value in options.items():
        car_dict[option] = value

    return car_dict

my_outback = make_car('subaru', 'outback', color='blue', tow_package=True)
print(my_outback)
