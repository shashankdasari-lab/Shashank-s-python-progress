#To check weather a number is positive negative or zero 


num=int(input("Enter a number:"))

if num == 0:
    print("The entered number is zero")
elif num < 0:
    print(f"The number {num} is negative")
else :
    print(f"The number {num} is positive")