#Week 7
#Regular expressions or “regexes” will enable us to examine patterns within our code.
#For example, we might want to validate that an email address is formatted correctly.
#Regular expressions will enable us to examine expressions in this fashion
email = input("What's your email? ").strip()

if "@" in email:
    print("Valid")
else:
    print("Invalid"

#You can imagine, however, that one could input @@
email = input("What's your email? ").strip()

if "@" in email and "." in email:
    print("Valid")
else:
    print("Invalid")

#We can improve the logic of our program as follows:
email = input("What's your email? ").strip()

username, domain = email.split("@")

if username and "." in domain:
    print("Valid")
else:
    print("Invalid")

#One of the most versatile functions within the library re is search.
import re

email = input("What's your email? ").strip()

if re.search("@", email):
    print("Valid")
else:
    print("Invalid")

#then
import re

email = input("What's your email? ").strip()

if re.search(".+@.+", email):
    print("Valid")
else:
    print("Invalid")

#now
import re

email = input("What's your email? ").strip()

if re.search(r".+@.+\.edu", email):
    print("Valid")
else:
    print("Invalid")
#“escape character” or \ as a way of regarding the . as part of our string instead of our validation expression
#Anchors specify where a match must occur. ^
#r"^hello"
#End of a string.$
#r"world$"

#Character classes define groups of characters.
#[a-z] Lowercase letters.
#[^@] The ^ inside square brackets means NOT.

#Regex patterns are usually written as raw strings
#The r tells Python to treat backslashes literally
