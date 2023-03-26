
class Point:
    def move(self):
        print("move")
    def draw(self):
        print("draw")

point1 = Point() # object of class
point1.move()
point1.x = 20 # attribute of object
point1.y = 10+point1.x
print(point1.y)

point2 = Point()
point2.draw()

# ---------- constructor ---------------

class Point:
    def __init__(self,x,y): # used to construct or create an object
        # self is reference to current object
        self.x = x # x argument passed to this function
        self.y = y # y argument passed to this function
    def move(self):
        print("move")
    def draw(self):
        print("draw")
# when we create new point object self reference to that

point1 = Point(10,20) # object of class
point1.x = 15
print(point1.x)
point2 = Point(2,4)
print(point2.y)


class Person:
    def __init__(self,name):
        self.name = name
    def talk(self):
        print(f"{self.name} Talking")


p1 = Person("Munaza")
p1.talk()
print(p1.name)

p2 = Person("Han")
p2.talk()

# ------------- inheritance -------------------------------

class Mammals:
    def __init__(self,animal):
        self.animal = animal
    def walk(self):
        print(f"{self.animal} walking")


class Dog(Mammals):
    # pyhton doesn't support empty class so we use pass
    pass # it means nothing, pass this line dw abt it


class Cat(Mammals):
    def des(self):
        print(f"{self.animal} is annoying")

cat1 = Cat("Scar The Cat")
cat1.walk()
cat1.des()

dog1 = Dog("Bruno The Dog")
dog1.walk()