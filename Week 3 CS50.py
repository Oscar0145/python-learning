#Week 3

#Exceptions are things that go wrong within our coding

# print("hello, world) has missing "

#In Python try and except are ways of testing out user input before something goes wrong

try:
    x = int(input("What's x?"))
    print(f"x is {x}")
except ValueError:
    print("x is not an integer")
    
#This is still not the best way to implement this code.
#Notice that we are trying to do two lines of code.
#For best practice, we should only try the fewest lines of code possible
#that we are concerned could fail

try:
    x = int(input("What's x?"))
except ValueError:
    print("x is not an integer")
else:
    print(f"x is {x}")


#Creating a function to get an integer
def main():
    x = get_int()
    print(f"x is {x}")


def get_int():
    while True:
        try:
            x = int(input("What's x?"))
        except ValueError:
            print("x is not an integer")
        else:
            return x


main()

#We can make it such that our code does not warn our user,
#but simply re-asks them our prompting question
def main():
    x = get_int()
    print(f"x is {x}")


def get_int():
    while True:
        try:
            return int(input("What's x?"))
        except ValueError:
            pass


main()


