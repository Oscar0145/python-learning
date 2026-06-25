#Week 4

#Libraries
#Generally, libraries are bits of code written by you or others that you can use in your program.

#random is a library that comes with Python that you could import into your own project
import random

coin = random.choice(["heads", "tails"])
print(coin)

#or

from random import choice

coin = choice(["heads", "tails"])
print(coin)

#Python comes with a built-in statistics library

import statistics

print(statistics.mean([100, 90]))

#sys is a module that allows us to take arguments at the command line.

import sys

print("hello, my name is", sys.argv[1])

#Our program can be improved as follows

import sys

if len(sys.argv) < 2:
    print("Too few arguments")
elif len(sys.argv) > 2:
    print("Too many arguments")
else:
    print("hello, my name is", sys.argv[1])

#slice is a command that allows us to take a list and tell the interpreter
#where we want the interpreter to consider the start of the list and the end of the list
import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv[1:]:
    print("hello, my name is", arg)

#A package is a collection of related modules
    

