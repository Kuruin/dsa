# keyword arg
from math import pi
from unicodedata import numeric

from numpy import fix


def increment(value, by=0):  # here the by is optional parameter,
    # be aware after an optional parameter, you cant add normal ones , so keep optional parameter at the end
    return (f"{value + 1}")


# we define what value a parameter should have
print(increment(2, by=1))
# or
print(increment(by=1, value=10))


# [] = lists
# () = tuple
# {} = dict

def multiply(*numbers):  # here the * makes it tuple
    total = 1
    for i in numbers:
        total *= i
    return total


print(multiply(5, 2, 3, 4))


def details(**user):  # ** is dictonary
    print(user['name'])


# for dict we pass key value pairs
details(id=1, name='manavjit', password='121')

# exercise


def fizz_buzz(n):
    if n == -1 or n == 0:
        print("Enter a valid number")
        return
    if (n % 5 == 0) and (n % 3 == 0):
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)


n = int(input("Your no: "))
fizz_buzz(n)
