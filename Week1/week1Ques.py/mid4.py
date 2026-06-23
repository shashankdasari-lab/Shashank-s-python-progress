"""Problem Statement

Accept a word from the user.

Determine whether it reads the same forward and backward.

Examples
madam
racecar
level"""

word=str(input("enter a word:"))
reverse=word[::-1]
print(reverse)
if word == reverse:
    print("palindrome")
else:
    print("not a palindrome")


