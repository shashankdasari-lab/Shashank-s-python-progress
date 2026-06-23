""""1. Username Validator ⭐
Problem Statement
Create a program that accepts a username from the user.
Requirements
A valid username must:
Have at least 5 characters
Must not contain any spaces
Must start with an alphabet
Output
Display:
Valid Username
or
Invalid Username"""



print("Create a username less than 5 characters ")
name=str(input("Enter username:"))
char=(len(name))
if char<=5:
    print("valid username")
else:
    print("invalid username")

    