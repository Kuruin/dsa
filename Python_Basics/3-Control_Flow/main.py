# ord for ASCII value
from math import pi


print(ord('a'))
temp = 30
if temp > 30:
    print("Warm")
else:
    print("cold")


# ternanry op
age = 10
message = "Eligible" if age >= 18 else "Not Eligible"
print(f'{message}')


# Logical op
income, age, credit = 100, 19, 1
if income > 100 and age > 18:  # or
    print("Eligible")
else:
    print("Not eligible")


student = False
if not student and income < 1000:  # not inverses the value of the boolean
    # it is short circuit,
    # eg if high_income and high_paying and not student
    # the evalutaion stops if we get one false, dosent matter if others are true ( only the case for AND)
    # for OR it dosent matter

    # Short-circuit evaluation:
    # AND: stops at first False
    # OR: stops at first True

    print("What are you doing")
else:
    print("GET A JOB")

# for loop
for i in range(0, 10, 2):  # (start,end,step)
    if i > 5:
        print(f"{i + 1}" + (i + 1) * ".")
        break

# iterable
for x in "hello":
    print(x)
for y in [1, 2, 3]:
    print(y)


# while loop
while True:
    i = input("Input here: ").lower()
    if (i == 'quit'):
        break

# excerise
count = 0
for i in range(1, 10):
    if i % 2 == 0:
        print(i)
        count += 1
    else:
        pass
print(f"We have {count} even no")
