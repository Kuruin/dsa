try:
    with open("a.py") as file:  # one dosent need a finally and a file.close() with, the with statement
        print("Inside the file")
    int(input("Enter a int: "))
    print("Noice!")
except (ValueError, FileNotFoundError) as x:
    print("What you doing nigga \n", x)
    # raise BaseException("Idhar ek exception aaya re londe")
    # rasing excep lead to performance issues for a large app
    # instead retrun none and compare to
    # if  a == None:
    #    pass
else:  # runs when no exceptions
    print("No excep")
finally:
    print("Hamesha Chalunga!")
