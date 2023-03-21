# --------------------- Function ---------------------------
# def is reserved keyword for function in pyhton i.e; short form of define
# syntax; def function_name():
def greet_user():
    print("Hello There!")
    print("Welcome to our studios")

print("START") # 2 block gap btw function definition and this statement cz pycharm said so, otherwise error 305
greet_user() # calling function
print("FINISH")


def greet_user():
    print("Hello!")

greet_user()


def greet_user(username):
    print("Hello, " + username.title() + "!")


greet_user('jesse')

# ------------------ Parameters in Function ------------------

def greet_user(msg1,msg2):
    print(msg1)
    print(msg2)


msg1 = "Welcome to Exploration"
msg2 = "Let's make this journey memorable together"
print("START")
greet_user(msg1,msg2)
print("FINISH")


def greet_user(name):
    print(f"Hello {name}!")
    print("Welcome to our studios")


name = input("Enter Your Name ")
print("START")


greet_user(name)
print("FINISH")


 # Positional Arguments (order matters with positional arguments)


def describe_pet(animal_type, pet_name):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet('hamster', 'harry')


def greet_user(fname,lname):
    print(f"Hello {fname} {lname}!")
    print("Welcome to our studios")


print("START")
greet_user(lname='Johnson', fname='Scarlett')
print("FINISH")


# Default Values

def describe_pet(pet_name, animal_type='dog'):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet(pet_name='willie')

describe_pet(pet_name='harry', animal_type='hamster')

# Equivalent Function Calls


def describe_pet(pet_name, animal_type='dog'):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet('willie')
describe_pet(pet_name='willie')

describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')

# Passing lists to Function
def greet_users(names):
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

# Modifying a List in a Function


def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
    print("Printing model: " + current_design)
    completed_models.append(current_design)


def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

# Mixing Positional and Arbitrary Arguments

def make_pizza(size, *toppings):
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)


make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


# USER INPUTS

name = input('What is your name? ')
dob = input('What is your date of birth? ')
p_year = input('What is present year? ')
age = int(p_year) - int(dob)
print(name+' is ', age , ' years old')


weight_inpounds = input('What is your weight in pound? ')
print(type(weight_inpounds))
weight_inkilogram = int(weight_inpounds)*0.45
print(type(weight_inkilogram))
print('Weight in kilogram : ',weight_inkilogram)


# ----------- Return statement --------------

def sq(number):
    return number*number


res = sq(9)
print(res)
print(sq(10))
number = int(input("Enter number: "))
print(sq(number))


# --------------------------------- Conditionals -------------------------------


price = 1000000
good_credit = True
if(good_credit):
    dp = price*0.1
else:
    dp = price*0.2
print(f'down payment: ${dp}')



x = 20

if (x>20):
    print('value entered is greater than 20')
elif(x<20):
    print('value entered is less than 20')
else:
    print('value entered is equal to 20')


# --------------------------- SET ----------------------------

myset = {"apple", "banana", "cherry"}
print(myset)


# Duplicate values will be ignored


thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)


# True and 1 is considered the same value:

sset = {"apple", "banana", "cherry", True, 1, 2}
print(sset)

# Get the Length of a Set

thisset = {"apple", "banana", "cherry"}
print(len(thisset))

# Set Items - Data Types

sset1 = {"apple", "banana", "cherry"}
print(sset1)
set2 = {1, 5, 7, 9, 3}
print(sset1)
set3 = {True, False, False}
print(sset1)


sett = {"abc", 34, True, 40, "male"}
print(sett)


# Printing data type of a set
myset = {"apple", "banana", "cherry"}
print(type(myset))


# set() constructor
thisset = set(("apple", "banana", "cherry"))
print(thisset)


# ------------------------- OPerations ON Sets ---------------------------------

A = {0, 2, 4, 6, 8};
B = {1, 2, 3, 4, 5};

# union
print("Union :", A | B)

# intersection
print("Intersection :", A & B)

# difference
print("Difference :", A - B)

# symmetric difference
print("Symmetric difference :", A ^ B)


# --------------------------------- Making Data Unique with Sets -------------------------------

def unique(numbers_list):
    unique_list = []
    for x in numbers_list:
        if x not in unique_list:
            unique_list.append(x)
            print(x)

numbers = input("Enter numbers of List: ")
numbers_list = numbers.split()

for i in range(len(numbers_list)):
    numbers_list[i] = int(numbers_list[i])


print("\nThe unique values of list is: ")
unique(numbers)


# ------------------------------ Timing The Code ----------------------------



# Using time module

import time
start = time.time()

print(23*2.3)

end = time.time()
print(end - start)


# Using timeit module

from timeit import default_timer as timer
start = timer()

print(23*2.3)

end = timer()
print(end - start)


import time

start = time.time()

a = 0
for i in range(1000):
    a += (i ** 100)
    print(a)

end = time.time()

print("The time of execution of above program is :",
      (end - start) * 10 ** 3, "ms")