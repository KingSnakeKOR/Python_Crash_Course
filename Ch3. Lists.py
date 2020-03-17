bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[0:2])
# print(bicycles.title()) - error
# print(bicycles[].title()) - error
# print(bicycles[:].title()) - error
# print(bicycles[0:].title()) - error
print(bicycles[0].title())

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

invitelist1 = ['Michael Jordan1', 'Tiger Woods1', 'Oprah1', 'Steve Jobs1', 'Warren Buffet1', 'Leonardo DiCaprio1']
print(invitelist1)
# print(invitelist1.reverse()) - you must do invitelist1.reverse() first, you can't do print(invitelist1.reverse())
# reverse is self! so inside the () you can not put in any argument
# print(invitelist1.reverse('Warren Buffet')) - error
# print(invitelist1.reverse(2)) - error

#invitelist1.title() - error
# this is because title method can only work for one set of string NOT the whole list
print(invitelist1[0].title())


# 3-1
names = ["josh", "sarah", "happy"]
print(names[0])
print(names[1])

# 3-2
message = "my friend's name is " + names[0].title() + "."
print(message)

# 3-4
invitelist = ['할아버지', '정주영', 'Steve Jobs']
print(invitelist[0], 'Please come have a dinner with me')
print(invitelist[1], 'Please come have a dinner with me')

# 3-5
invitelist.pop(0)
invitelist.append('Warren Buffet')
print(invitelist[0], 'Please come have a dinner with me')
print(invitelist[1].title(), 'Please come have a dinner with me')
print(invitelist)

# 3-6
print("Goodnews, we can invite more guests")
invitelist.insert(0, "Michael Jordan")
invitelist.insert(2, "이순신")
invitelist.append("Leonardo DiCaprio")
print(invitelist[0], 'Please come have a dinner with me')
print(invitelist[1].title(), 'Please come have a dinner with me')
print(invitelist[2].title(), 'Please come have a dinner with me')
print(invitelist)

# 3-7 ***
print(len(invitelist))
print("I can only invite two people, sorry")
popped = invitelist.pop()
print("Hey", popped, "sorry you are not invited")
popped = invitelist.pop()
print("Hey", popped, "sorry you are not invited")
popped = invitelist.pop()
print("Hey", popped.title(), "sorry you are not invited")
popped = invitelist.pop()
print("Hey", popped, "sorry you are not invited")
print(invitelist)
print(invitelist[0], 'you are still invited')
print(invitelist[1].title(), 'you are also still invited')
del invitelist[0]
del invitelist[0]
print(invitelist)

#invitelist = ['Michael Jordan', 'Tiger Woods', 'Oprah', 'Steve Jobs', 'Warren Buffet', 'Leonardo DiCaprio']
#print(len(invitelist))
#print(invitelist)
#invitelist.pop()
#print(invitelist)
#print("Hey", invitelist.pop(), "sorry you are not invited")
# 여기서 pop하고 run하면 나타나지는 않지만 pop을 하고 print에서 또 pop을 한거니깐 두번한걸로 된다!!!!!!!!!!!!
# 그러니깐 invitelist.pop() = popped 로 해야 두번 안되고 똑같은 걸로 계속 된다
#invitelist.pop()
#print("Hey", invitelist.pop(), "sorry you are not invited")
#invitelist.pop()
#print("Hey", invitelist.pop(), "sorry you are not invited")
#invitelist.pop()
#print("Hey", invitelist.pop(), "sorry you are not invited")
#print(invitelist)
#print(invitelist[0], 'you are still invited')
#print(invitelist[1].title(), 'you are also still invited')
#del invitelist[0]
#del invitelist[0]
#print(invitelist)

# 3-8
locations = ['Cabo', 'Greece', 'Italy', 'Indonesia', 'Vietnam']
print(locations)
print(sorted(locations))
print(locations)
#print(sorted(locations.reverse())) - TypeError: 'NoneType' object is not iterable
print(sorted(locations, reverse = True))
print(locations)
#print(locations.reverse()) - error
locations.reverse()
print(locations)
locations.sort()
print(locations)
locations.sort(reverse = True)
print(locations)
