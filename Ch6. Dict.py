alien_0 = {'color':'green', 'points':5}
print(alien_0['color'])
#add new pairs
alien_0['x_position'] = 0
alien_0['y_position'] = 25

#modify the value
alien_0['color'] = 'yellow'

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_0['x_position']))
# I don't need to define x_increment!!
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New position: " + str(alien_0['x_position']))

del alien_0['speed']

# 6-1
# for a long list of dictionary use the below format
person = {'first_name':'michael',
          'last_name':'smith',
          'age':'27',
          'city':'Seoul'
          }
print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['city'])

# 6-2
favorite_numbers = {'michael':9, 'jenny':3, 'sue':6, 'ryan':3336, 'spencer':7}
print("Hey michael's favorite number is" + str(favorite_numbers['michael']))

# 6-3
python_words = {'for':'loop',
                'if':'conditional',
                'list':'collection',
                'dict':'key-value',
                'python':'conquer'
                }
print("In python 'for' stands for: " + python_words['for'])
print("\nIn python 'if' stands for: " + python_words['if'])

user_0 = { 'username': 'xxx',
           'first':'michael',
           'last':'smith'
           }
for key, value in user_0.items():
    print("Key: " + key)
    print("Value: " + value)

# keys method
favorite_languages = {'jen' : 'python',
                      'sarah' : 'c',
                      'edward' : 'ruby',
                      'phil':'python'
                      }

friends = ['phil', 'sarah']
#for name in favorite_languages.keys(): = for name in favorite_languages.keys():  because the key is the default behavior when looping thru dict
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        print("Hi, " + name.title() + " I see your favorite language is " + favorite_languages[name].title())

if 'erin' not in favorite_languages.keys():
    print('Erin, please take a poll')

# values method
print("The following languages have been mentioned: ")
for language in favorite_languages.values():
    print(language.title())
# set - identifies the unique items in the list and builds a set from those items (don't count the same thing twice!)
for language in set(favorite_languages.values()):
    print(language.title())

# 6-4
python_words = {'for':'loop',
                'if':'conditional',
                'list':'collection',
                'dict':'key-value',
                'python':'conquer'
                }
for word in python_words.keys():
    print("In python " + "'" + word + "'" + " stands for " + python_words[word])

# Textbook answer
for word1, definition in python_words.items():
    print(word1 + ":" + definition)
# items - returns a list of key-value pairs

# 6-5
rivers_country = {'nile':'egypt',
                  'hangang':'south korea',
                  'thames':'england'
                  }

for river, country in rivers_country.items():
    print("The " + river + " runs through " + country)
for river1 in rivers_country.keys():
    print(river1)
for country1 in rivers_country.values():
    print(country1)

# 6-6
favorite_languages = {'jen' : 'python',
                      'sarah' : 'c',
                      'edward' : 'ruby',
                      'phil':'python'
                      }
friends = ['jen', 'ryan', 'jill', 'phil']

for friend in friends:
    if friend in favorite_languages.keys():
        print(friend.title() + ' thank you')
    else:
        print(friend.title() + ' take a poll')

#for friend_list in favorite_languages1.keys(): - 진짜 생각이 없다 이게 Matching한다고 생각을 했지 LOOP인데!!!!!
    #print(friend_list)
    #if friend_list in friends1:
        #print(friend_list + " Thank you")
    #if friend_list not in friends1:
        #print(friend_list + " take a poll")

    #if friend_list in friends:
        #print(friends + " Thank you for taking the poll")
    #else:
        #print(friends + "Please take a poll")

   #if friends in friend_list:
        #print(friends + "Thank you for taking the poll")
    #if friends not in favorite_languages.keys():
        #print(friends + "Please take a poll")

# Dict inside of a List
# Make an empty list for storing aliens
aliens = []
# Make 30 green aliens
for alien_number in range(30):
    new_alien = {'color':'green', 'points':5, 'speed':'slow'}
    aliens.append(new_alien)

# Change the 3 aliens
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['sped'] = 'medium'

# Show the first 5 aliens
for alien in aliens[0:5]:
    print(aliens)
print("......")

#Show how many aliens have been created
print("Total number of aliens: " + str(len(aliens)))

# Dict inside a list
# Store information about a pizza being ordered
pizza = {'crust':'thick', 'toppings':['mushrooms', 'extra cheese']}

# Summarize the order
print("You orderd a " + pizza['crust'] + "-crust pizza " + "with the following toppings")

for topping in pizza['toppings']:
    print("\t" + topping)
# You can nest a list inside a dictionary any time you want more than one value to be associated with a single key in a dictionary.

# 6-7
person_0 = {'first_name':'michael', 'last_name':'smith', 'age':'27', 'city':'Seoul'}
person_1 = {'first_name':'jenny', 'last_name':'herber', 'age':'21', 'city':'Daegu'}
person_2 = {'first_name':'howard', 'last_name':'james', 'age':'34', 'city':'Tokyo'}
people = [person_0, person_1, person_2]

for person in people:
    print("First name: " + person['first_name'].title())
    print("Last name: " + person['last_name'].title())
    print("Age: " + person['age'])
    print("City: " + person['city'].title())
# Textbook answer
# people.append(person_0)

# 6-8
pets = []
pet_1 = {'animal type': 'python', 'name': 'john', 'owner': 'guido'}
pets.append(pet_1)

pet_2 = {'animal type': 'dog', 'name': 'ryan', 'owner': 'howard'}
pets.append(pet_2)

for pet in pets:
    #for key, value in pet:
    for key, value in pet.items():
        print("Here is the following information: " + key.title() + " is " + value.title())
# Textbook answer
for pet in pets:
    print("\nHere's what I know about " + pet['name'].title() + ":")
    for key, value in pet.items():
        print("\t" + key + ": " + str(value))

# 6-9
favorite_places = {'james': ['seoul', 'new york'], 'happy':['cabo','cebu','hawaii']}
for name, places in favorite_places.items():
    print(name.title() +"'s favorite places are: ")
    for place in places:
        print("- " + place.title())

# 6-10
favorite_numbers = {'michael': [9, 88], 'jenny':[3, 36, 33], 'sue':[6, 5.5], 'ryan':[3336, 17], 'spencer':[7]}
for name, numbers in favorite_numbers.items():
    print("Hey " + name.title() + "'s favorite numbers are: ")
    for number in numbers:
        print("- " + str(number))

# 6-11
cities = {
    'santiago': {
        'country': 'chile',
        'population': 6158080,
        'nearby mountains': 'andes',
        },
    'talkeetna': {
        'country': 'alaska',
        'population': 876,
        'nearby mountains': 'alaska range',
        },
    'kathmandu': {
        'country': 'nepal',
        'population': 1003285,
        'nearby mountains': 'himilaya',
        }
    }

for names, infos in cities.items():
    print(names.title() + "'s info: ")
    for category, info in infos.items():
        print(category.title() + " : " + str(info).title())
