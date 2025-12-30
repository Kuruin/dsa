from array import array
from collections import deque

# lists
from encodings import mac_arabic
import enum
from http.cookiejar import CookieJar
import re
from traceback import print_tb


letters = ['a', 'b', 'c', 'd']
matrix = [[1, 2], [3, 4]]
zeros = [0] * 10
combined = zeros + letters  # concatenated
print(len(letters))
test = list(range(5))
test1 = list("HEllo WORLD")
print(test1[0:3])
print(test1[-1])
print(test1[::2])  # here 2 is the step

# unpacking
no = [1, 2, 3, 4, 5, 6, 7, 8, 9]
no1, no2, *others = no
no1, *others, last = no


# iterate over lists
test4 = ['a', 'b', 'c', 'd']
for index, letter in enumerate(test4):  # IMP
    print(index, letter)

# methods
test4.append('e')  # last mein add karo
print(test4)
test4.insert(0, 'what')  # posi pe add karo
print(test4)

test4.pop(0)  # posi pe nikalo
print(test4)
# remove the first occurence of the letter, useful when dont know the posi of the letter
test4.remove('b')
print(test4)
print(test4.index('c'))
test4.clear()  # pura saaf kardo
print(test4)

sortMe = [
    ('P1', 10),
    ('P2', 120),
    ('P3', 30),
]
# lambda functions
# lambda parameters:expressions
sortMe.sort(key=lambda x: x[1], reverse=True)
print(sortMe)

# map
prices = list(map(lambda item: item[1], sortMe))
print(prices)

# filter
test6 = list(filter(lambda x: x > 5, no))
print(test6)


# list comphrensions
test7 = [i[1] for i in sortMe]  # alt for map
print(test7)
test7 = [i[1] for i in sortMe if i[1] > 20]  # alt for filter we add the if
print(test7)

# zip
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
print(list1 + list2)
print(list(zip(list1, list2)))

# stack
stack = [1, 2, 3]
print(stack)
stack.append(4)
print(stack)
stack.append(5)
print(stack)
stack.pop()
print(stack)
if not stack:
    print("empty")


# queue
queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
print(queue)
queue.popleft()
print(queue)
if not queue:
    print("empty")

# tuples
# they are immutable
wowTuple = (1, 2, 3, 4, 1)
tupleEg = 1,  # this a tuple too
tupleEg = 1, 2  # this a tuple too
print(wowTuple[0])
print(wowTuple[0:2])
if 10 in wowTuple:
    print("Exists")
print(wowTuple.count(1))

# swap variables
x = 10
y = 11
x, y = y, x
print(x, y)

# array
test7 = array("i", [1, 2, 3, 4])
print(test7)
# varieous methods are available

# sets - unordered collections, ie we cant access it by index
# denoted by {}
set1 = {1, 2, 3}
set2 = {4, 5, 1}
print(set1 | set2)  # union
print(set1 & set2)  # intersection
print(set1 - set2)  # diff
print(set1 ^ set2)  # sematic diff

# dictonary
dict1 = {'x': 1, "y": 2}
print(dict1)
# or
dict2 = dict(z=10, u=1)
print(dict2)
for key in dict1:
    print(key, dict1[key])

# or
for key, value in dict2.items():
    print(key, value)

# . and access all the methods

# dict comprehension
# values1 = [expression for item in items]
values1 = {a: a * 2 for a in no}  # when we do for tuple we ge generator
print(values1)

# generator
# they dont store items in memory
genTest1 = (values * 2 for values in range(5))
for i in genTest1:
    print(i)


# unpacking operator
# we can unpack any iterable
view = [*range(5), *"HEllo"]
print(view)
view2 = {"x": 1, "y": 2}
out = {**view2}
print(out)


# exercise
science = 'This is a common interview question'
char_freq = {}
for char in science:
    if char in char_freq:
        char_freq[char] += 1
    else:
        char_freq[char] = 1
print(char_freq)
listToSort = list(char_freq.items())
maxCount = sorted(listToSort, key=lambda kv: kv[1], reverse=True)[0]
print(maxCount)
