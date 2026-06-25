#Week 2

#Instead of
print("Hello")
print("Hello")
print("Hello")

#Use
for i in range(3):
    print("Hello")

#A for loop repeats code a fixed number of times or iterates over a sequence
#range() generates a sequence of numbers

#A while loop continues running while a condition is true
count = 1
while count <= 5:
    print(count) count += 1

#If the loop condition never becomes false, the program runs forever
#break immediately exits a loop
#continue skips the rest of the current iteration and moves to the next one

#Nested loops
#A loop can contain another loop.
for row in range(3):
    for column in range(4):
        print("*", end="")
    print()
