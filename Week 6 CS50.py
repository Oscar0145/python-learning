#Week 6

#File I/O is the ability of a program to take a file as input or create a file as output.
#list is a data structure that allows us to store multiple values into a single variable.
names = []

for _ in range(3):
    name = input("What's your name?" )
    names.append(name)

#open is a functionality built into Python
#that allows you to open a file and utilize it in your program.
#The open function allows you to open a file such that you can read from it or write to it.
name = input("What's your name? ")

file = open("names.txt", "w")
file.write(name)
file.close()
#Notice that the open function opens a file
#called names.txt with writing enabled, as signified by the w
name = input("What's your name? ")

file = open("names.txt", "a")
file.write(name)
file.close()
#we want to be able to append each of our names to the file.
#Remove the existing text file by typing rm names.txt in the terminal window.

#The keyword with allows you to automate the closing of a file.
name = input("What's your name? ")

with open("names.txt", "a") as file:
    file.write(f"{name}\n")

#CSV stands for “comma separated values”.
with open("students.csv") as file:
    for line in file:
        row = line.rstrip().split(",")
        print(f"{row[0]} is in {row[1]}")
#or
with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        print(f"{name} is in {house}")
