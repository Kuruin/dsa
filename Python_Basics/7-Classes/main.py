from operator import getitem
from tkinter import S


class Point:

    default_color = 'red'
    # all methods should atleast have one parameter, self
    # here self is a reference to the object

    def __init__(self, x, y):  # these are magic methods __sdsd__ vale
        self.x = x
        self.y = y  # these are instance attributes

    def set_posi(self):
        print(f"Points are {self.x}, {self.y}")

    @classmethod
    def thisIsAClassMethod(cls):
        print("Ye class method hain")


point = Point(1, 2)
print(point.set_posi())
point.default_color = 'blue'
print(point.default_color)  # this is an instance

# this is an class attribute, can be accessed throughout the class
print(Point.default_color)

# this is a class method, and how to access them
print(Point.thisIsAClassMethod())


######
class TagCloud:
    def __init__(self):
        self.tags = {}

    def add(self, tag):
        self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return self.tags[tag]

    def __setitem__(self, tag, count):
        self.tags[tag.lower()] = count

    def __iter__(self):
        return iter(self.tags)


cloud = TagCloud()
cloud.add("Python")
cloud.add("python")
cloud.add("python")
print(cloud.tags)
print(cloud['python'])
cloud['jAva'] = 10
print(cloud.tags)
for i in cloud:
    print(i)
######


# private members
class TagCloud2:  # here the __ is private, hypothetical, we can still access them
    def __init__(self):
        self.__tags = {}

    def add(self, tag):
        self.__tags[tag.lower()] = self.tags.get(tag.lower(), 0) + __1

    def __getitem__(self, tag):
        return self.__tags[tag]

    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    def __iter__(self):
        return iter(self.tags__)


cloud2 = TagCloud2()
print(cloud2.__dict__)
#  o/p =
# {'_TagCloud2__tags': {}}
#
print(cloud2._TagCloud2__tags)


# revise it
class Product:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter  # if we dont set the setter, then its read only
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self.__price = value


test = Product(1)
print(test.price)


class Animal:
    def __init__(self):
        self.x = 10

    def eat(self):
        print("It eats ")


class Mammal(Animal):  # animal is the base class
    # method overriding means, replacing or extending a method in the base class
    # print(m.x) # because it got overriden by the Mammal class constructor
    # to prevent this use super
    def __init__(self):
        super().__init__()  # call the constructor of the Animal class, so it dosent replace it
        self.y = 1

    def idk(self):
        print("IDK")


m = Mammal()
print(m.eat())
print(issubclass(Mammal, object))
print(issubclass(Mammal, Animal))
# here the object is the base class inherited by default by every class :)
print(issubclass(Animal, object))
print(m.x)

# AVOID MULTI LEVEL INHERITANCE, MAX 1-2 LEVEL
