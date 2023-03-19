# ---------------------------------- Strings -----------------------------------------

print("Hello BWFs!")

message = "Don't know what to type"
print(message)
# allows you to use quotes and apostrophes within your strings:
str = 'Munaza and Marco'
str1 = "Munaza's Macrco"
print(str1 + '/' + str)

msg = 'I told my friend, "Python is my favorite language!"'
msg1 = "The language 'Python' is named after Monty Python, not the snake."
msg2 = "One of Python's strengths is its diverse and supportive community."
print(msg)
print(msg1)
print(msg2)

# concatenating strings
owner = 'Munaza'
pet = 'Marco'
message = pet + ' is ' + owner +"'s pet"      # two ways to concatenate strings
print(message)
msg = f"{pet} is {owner}'s pet"   # f is for formatted strings, no need to use + or ,
print(msg)

# writing strings line by line
sstr = '''
I told my friend, Python is my favorite language!
The language 'Python' is named after Monty Python, not the snake.
One of Python's strengths is its diverse and supportive community.
'''
print(sstr)
#Changing Case in a String with Methods
name = "munaza's marco"
print(name.title())
# changing a string to all uppercase or all lowercase letters
print(name.upper())
print(name.lower())

first_name = "Munaza"
last_name = "Ashraf"
nname = first_name + " " + last_name

pp = "Hello" + " " + nname.title() + "!"
print(pp)

print("Python")
# Adding Whitespace to Strings with Tabs
print("\tPython")
# Adding Whitespace to Strings with Newline
print("Languages:\nPython\nC\nJavaScript")

# Stripping Whitespace
txt = "   banana     "
x = txt.rstrip()
print("of all fruits", x, "is my favorite")

txt = "    banana     "
y = txt.lstrip()
print("of all fruits", y, "is my favorite")

txt = "    banana     "
z = txt.strip()
print("of all fruits", z, "is my favorite")


# -------------------------- Integers ------------------------

print (10+3)
print (10-3)
print (10*3)
print (10/3)
print (10//3)
print (10%3)
print (10**3)
print(2**3)

x = 20
x = x + 30
print(x)
x += 30
print(x)


print(3 ** 2)
print(3 ** 3)
print(10 ** 6)

print(2 + 3*4)
print((2 + 3) * 4)

x = 10 + 3 * 2
print(x)  # operator precedence (1. paranthesis   2. exponent, 3. Multiplication/Division,  4. Addition/Subtraction)
x = 10 + 3* 2**2
print(x)
x = (10 + 3)* 2**2
print(x)

# -------------------------- Floats ------------------------

print(0.1 + 0.1)
print(0.2 + 0.2)
print(2 * 0.1)
print(2 * 0.2)
print(0.2 + 0.1)
print(3 * 0.1)

# ---- can you please help me with that i have studied from various site but couldn't find the solution
# Avoiding Type Errors with the str() Function
# age = 28
# me "Happy " + str(age) + "rd Birthday!"
# print(me)

name = input('What is your name? ')
dob = input('What is your date of birth? ')
p_year = input('What is present year? ')
age = int(p_year) - int(dob) # type conversion from string to int
print(name+' is ', age , ' years old')

print(3/2)

print(3.0 / 2)
print(3 / 2.0)
print(3.0 / 2.0)

# Zen of Python
import this

# ------------------------- Lists ---------------------------------

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
# When we ask for a single item from a list, Python returns just that element without square brackets or quotation  marks
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[-1]) # - will start taking elements from the end of list
print(bicycles[-2])

message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)

str1 = "Munaza's Marco"  # both double and single quotations can be used to write strings
print(str1)
print(str1[0],str1[1],str1[-1],str1[-5]) # in python string index starts from 0, it will print values at the given indexes in sq. bracket
print(str1[0:5])
print(str1[0:])
print(str1[:6])
print(str1[:])
print(str1[0:-1])
str2 = 'Marco is a "pomeranian" breed'
print(str2)
str = str2[:]
print(str)


# Modifying Lists
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

# Adding Elements to a List

# Appending Elements to the End of a List
motorcycles.append('ducati')
print(motorcycles)

motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

# Inserting Elements into a List

motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati') # with this you can tell where you want to insert new value
motorcycles.insert(2, 'vb') # it will be added first to 2nd index
motorcycles.insert(2, 'hyundai') # then it will added to 2nd index
print(motorcycles)

# Removing Elements from a List
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[0] # del permanently delete values from lists
print(motorcycles)
del motorcycles[1]
print(motorcycles)

# Removing an Item Using the pop() Method
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop() # remove from last
print(motorcycles)
print(popped_motorcycle)

motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print("The last motorcycle I owned was a " + last_owned.title() + ".")

# Popping Items from any Position in a List
first_owned = motorcycles.pop(0)
print('The first motorcycle I owned was a ' + first_owned.title() + '.')

# Removing an Item by Value

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")

# Sorting a List Permanently with the sort() Method

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
print("\nHere is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)

# Finding the Length of a List

str = 'Munaza is the coolest'
print(len(str))
print(str.upper())
print(str.lower())
print(str.find('s'))  # print the index 's' is present otherwise print -1
print(str.find('S'))
print(str.find('coolest'))   # print starting index from where coolest is starting
print(str.replace('coolest','dumbest'))   # replaces coolest with dumbest
str = 'Munaza is the coolest'
print('coolest' in str)   # find the coolest word in string but different is that it doesn't print index, it prints true or false
print('Coolest' in str)
print(str.title())# Sorting a List Permanently with the sort() Method

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
print("\nHere is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)

# Finding the Length of a List

str = 'Munaza is the coolest'
print(len(str))
print(str.upper())
print(str.lower())
print(str.find('s'))  # print the index 's' is present otherwise print -1
print(str.find('S'))
print(str.find('coolest'))   # print starting index from where coolest is starting
print(str.replace('coolest','dumbest'))   # replaces coolest with dumbest
str = 'Munaza is the coolest'
print('coolest' in str)   # find the coolest word in string but different is that it doesn't print index, it prints true or false
print('Coolest' in str)
print(str.title())

# ------------------------- Loops -----------------------------------

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

for magician in magicians:
    print(magician.title() + ", that was a great trick!")

for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")
print("Thank you, everyone. That was a great magic show!")


is_hot = True
is_cold = False
if (is_hot):
    print("""It's a hot day
Eat icecream""")
elif (is_cold):
    print("""It's a cold day
Drink alot of soup""")
else:
    print(" What a lovely day")
    print('Enjoy your day')


price = 1000000
good_credit = True
if(good_credit):
    dp = price*0.1
else:
    dp = price*0.2
print(f'down payment: ${dp}')

char = 'lahoreqalandarsisWteam'
if(len(char)<3):
    print("\nname must be at least 3 characters")
elif(len(char)>50):
    print("\nName can be a max of 50 characters")
else:
    print("\nName looks good!")

i = 1
while (i<=5):
    print(i)
    i += 1
print("  DONE")

secret_number = 12
guess_count = 0
guess_limit = 3
while(guess_count<guess_limit):
    guess = int(input("Guess: "))
    guess_count += 1
    if guess == secret_number:
        print("  You win!")
        break
else:
    print("  You lose!")

for value in range(1,5):  #
    print(value)

# Using range() to Make a List of Numbers
numbers = list(range(1,6))
print(numbers)

# e range() function starts with the value 2 and then adds 2 to that value. It adds 2 repeatedly until it reaches or passes the end value, 11
even_numbers = list(range(2,11,2))
print(even_numbers)

squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
print(squares)

squares = [value**2 for value in range(1,11)]
print(squares)

# Simple Statistics with a List of Number

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

# Looping through slice

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

print("\n")
for player in players[3:]:
    print(player.title())

print("\n")
for player in players[-3:]:
    print(player.title())


my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

# ------------------------------- Tuples -------------------------
tuples = (1,2,3,5,8)
print(tuples[1])
print(tuples[0:3])

# cant modify Tuples
# When compared with lists, tuples are simple data structures. Use them
# when you want to store a set of values that should not be changed throughout the life of a program.


