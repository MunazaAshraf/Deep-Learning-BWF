
# --------------------- Docstrings ----------------------------
def square(n):
    '''Takes in a number n, returns the square of n'''
    print(n**2)


# Here, the string literal:
# '''Takes in a number n, returns the square of n'''
# Inside the triple quotation marks is the docstring of the function square() as it appears right after its definition.
num = int(input("Enter the number"))
square(num)

# ------------ enumerate() function ------------------------
# The enumerate() function takes a collection (e.g. a tuple) and returns it as an enumerate object.
#The enumerate() function adds a counter as the key of the enumerate object.
x = ('apple', 'banana', 'cherry')
y = enumerate(x)
print(y)
print(list(y))

l1 = ["eat", "sleep", "repeat"]
s1 = "geek"

# creating enumerate objects
obj1 = enumerate(l1)
obj2 = enumerate(s1)

# syntax enumerate(iterable, start)
print ("Return type:", type(obj1))
print (list(enumerate(l1)))

# changing start index to 2 from 0
print (list(enumerate(s1, 2)))

# ---------- Unique sets with Sets --------------------
# in lab 5 i made that with lists my mistake so heres the correct solution for that

# sets don't take duplicate values
student_id = {112, 114, 114, 116, 116, 118, 115}
print('Student ID:', student_id)

vowel_letters = {'a', 'e', 'i', 'o', 'u', 'u', 'a'}
print('Vowel Letters:', vowel_letters)

mixed_set = {'Hello', 101, -2, True, True, 'Bye'}
print('Set of mixed data types:', mixed_set)
