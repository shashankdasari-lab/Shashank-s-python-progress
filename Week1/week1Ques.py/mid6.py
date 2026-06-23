'''6. Dictionary Phone Book ⭐⭐
Problem Statement

Create a phone directory using a dictionary.

Store details of 5 people.

Ask User

Enter a person's name.'''

dict={
    "Shashank": 6309376721,
    "Dakshitha": 7013671745,
    "Charan": 9939935551,
    "Nishith": 7416310206,
    "Alivelu": 6309376721
}

name=str(input("Enter the name of the person you want search:"))
name=name.capitalize()
print(name)

if name == "Shashank":
    print("Shashank Phone number:",dict["Shashank"])
elif name == "Dakshitha":
    print("Dakshitha Phone number:",dict["Dakshitha"])
elif name == "Charan":
    print("Charan Phone number:",dict["Charan"])
elif name == "Nishith":
    print("Nishith Phone number:",dict["Nishith"])
elif name == "Alivelu":
    print("Alivelu Phone number:",dict["Alivelu"])
else:
    print("Name not valid")