name1=str(input("Enter name of student 1:"))
branch1=str(input("Enter your branch:"))
cgpa1=float(input("Enter your CGPA:"))
fi1=int(input("Enter your family income:"))

name2=str(input("Enter name of student 2:"))
branch2=str(input("Enter your branch:"))
cgpa2=float(input("Enter your CGPA:"))
fi2=int(input("Enter your family income:"))

name3=str(input("Enter name of student 3:"))
branch3=str(input("Enter your branch:"))
cgpa3=float(input("Enter your CGPA:"))
fi3=int(input("Enter your family income:"))

name4=str(input("Enter name of student 4:"))
branch4=str(input("Enter your branch:"))
cgpa4=float(input("Enter your CGPA:"))
fi4=int(input("Enter your family income:"))

name5=str(input("Enter name of student 5:"))
branch5=str(input("Enter your branch:"))
cgpa5=float(input("Enter your CGPA:"))
fi5=int(input("Enter your family income:"))

data={
    "student-1":{
        "name": name1,
        "branch": branch1,
        "cgpa": cgpa1,
        "family income": fi1
    },

    "student-2":{
        "name": name2,
        "branch": branch2,
        "cgpa": cgpa2,
        "family income": fi2
    },

    "student-3":{
        "name": name3,
        "branch": branch3,
        "cgpa": cgpa3,
        "family income": fi3
    },

    "student-4":{
        "name": name4,
        "branch": branch4,
        "cgpa": cgpa4,
        "family income": fi4
    },

    "student-5":{
        "name": name5,
        "branch": branch5,
        "cgpa": cgpa5,
        "family income": fi5
    }
}

print("\n===== ALL STUDENTS =====\n")

print(data["student-1"])
print(data["student-2"])
print(data["student-3"])
print(data["student-4"])
print(data["student-5"])

print("\n===== SCHOLARSHIP ELIGIBILITY =====\n")

if cgpa1 >= 8.5 and fi1 < 500000:
    print(name1, "- Eligible")
else:
    print(name1, "- Not Eligible")

if cgpa2 >= 8.5 and fi2 < 500000:
    print(name2, "- Eligible")
else:
    print(name2, "- Not Eligible")

if cgpa3 >= 8.5 and fi3 < 500000:
    print(name3, "- Eligible")
else:
    print(name3, "- Not Eligible")

if cgpa4 >= 8.5 and fi4 < 500000:
    print(name4, "- Eligible")
else:
    print(name4, "- Not Eligible")

if cgpa5 >= 8.5 and fi5 < 500000:
    print(name5, "- Eligible")
else:
    print(name5, "- Not Eligible")

print("\n===== TOPPER =====\n")

highest_cgpa = max(cgpa1, cgpa2, cgpa3, cgpa4, cgpa5)

if highest_cgpa == cgpa1:
    print("Topper:", name1, "-", cgpa1)

elif highest_cgpa == cgpa2:
    print("Topper:", name2, "-", cgpa2)

elif highest_cgpa == cgpa3:
    print("Topper:", name3, "-", cgpa3)

elif highest_cgpa == cgpa4:
    print("Topper:", name4, "-", cgpa4)

else:
    print("Topper:", name5, "-", cgpa5)