# ---------------------- Read File ----------------------
# count vowels in a string
def count_vowels(string_input):
    vowels = {'a','e','i','o','u'}
    num_vowels = 0
    for x in string_input:
        if x in vowels:
            num_vowels += 1
    return num_vowels

with open("file.txt",'r') as file:
    var = file.read()
    print(var)
    print(var[0:6])
    print(count_vowels(var))
    file.close()
    pass

# --------------- Append Mode --------------

with open("file.txt",'a') as file:
    file.write(" I am working on BWF's Task 09.")
    file.close()
    pass

with open("file.txt",'r') as file:
    var = file.read()
    print(var)
    file.close()
    pass

# ------------------- Write Mode ----------------------
with open("file.txt",'w') as file:
    file.write("Strings has been removed due to write mode.")
    file.close()
    pass

with open("file.txt",'r') as file:
    var = file.read()
    print(var)
    file.close()
    pass

# write helps in creating new files
with open("newfile.txt",'w') as file:
    file.write("Okay! So This is a new file")
    file.close()
    pass

with open("newfile.txt",'r') as file:
    var = file.read()
    print(var)
    print(type(var))
    file.close()
    pass

# --------------- Exceptions ----------------
# syntax
# try:
       # Some Code....
# except:
       # optional block
       # Handling of exception (if required)
# else:
       # execute if no exception
#finally:
      # Some code .....(always executed)

# Python code to illustrate
# working of try()
def divide(x, y):
    try:
        # Floor Division : Gives only Fractional
        # Part as Answer
        result = x // y
    except ZeroDivisionError:
        print("Sorry ! You are dividing by zero ")
    else:
        print("Yeah ! Your answer is :", result)
    finally:
        # this block is always executed
        # regardless of exception generation.
        print('This is always executed')

    # Look at parameters and note the working of Program

divide(3, 2)
divide(3, 0)

# exit code 0 means program ran successfully
# exit code 1 means program ran unsuccessfully
# Handles Error
# helps your program to not crash even if user enters wrong value
try:
    age = int(input("Enter your age: "))
    income = 2000
    risk = income/age
    print(age)
except ValueError:
    print("INVALID VALUE")
except ZeroDivisionError:
    print("Age can't be zero")




