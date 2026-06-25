#Week 1

#A Boolean can only have one of two values: True or False
print(5 > 3)

#The if statement executes code only if a condition is true.
age = 20

if age >= 18:
    print("You are an adult.")

#else runs when the if condition is false.
age = 15
if age >= 18:
    print("Adult")

else:
    print("Minor")

#elif allows multiple conditions to be checked.
score = 75
if score >= 70:
    print("First")
elif score >= 60:
    print("Upper Second")
elif score >= 50:
    print("Lower Second")
else:
    print("Fail")

#Logical operators combine multiple conditions.
age = 20
student = True
if age >= 18 and student:
    print("Eligible")

if age >= 18 or student:
    print("Access granted")

logged_in = False
if not logged_in:
    print("Please log in.")
