#age group categorization

age=int(input("Enter your age :"))

if age <= 9 and age >= 0:
    print("Child")
elif age <= 18 and age > 9:
    print("Teenager")
elif age <= 60 and age > 18 :
    print("Adult")
elif age < 0:
    print("invalid age")
else:
    print("Senior Citizen")