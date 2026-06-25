#Week 5

#A unit test checks whether a small part of a program works correctly

from calculator import square


def main():
    test_square()


def test_square():
    if square(2) != 4:
        print("2 squared was not 4")
    if square(3) != 9:
        print("3 squared was not 9")


if __name__ == "__main__":
    main()

#Python’s assert command allows us to tell the interpreter that something, some assertion,
#is true

from calculator import square


def main():
    test_square()


def test_square():
    assert square(2) == 4
    assert square(3) == 9


if __name__ == "__main__":
    main()

#pytest is a third-party library that allows you to unit test your program.
#That is, you can test your functions within your program
from calculator import square


def main():
    test_square()


def test_square():
    assert square(2) == 4
    assert square(3) == 9
    assert square(-2) == 4
    assert square(-3) == 9
    assert square(0) == 0

#We can change our hello function within hello.py as follows:
def main():
    name = input("What's your name? ")
    print(hello(name))


def hello(to="world"):
    return f"hello, {to}"


if __name__ == "__main__":
    main()

