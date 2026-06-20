#student mark calculator
"""Create a program that stores and processes a student's academic information.

Input

Take:

Student Name
Roll Number
Subject 1 Marks
Subject 2 Marks
Subject 3 Marks
Processing

Calculate:

Total Marks
Average Marks"""

print("\nStudent Mark Calculator\n")
print("Enter your marks out of 100\n")
name = str(input("Enter your name: "))
roll_number = str(input("Enter your roll number: "))
subject1_marks = float(input("Enter marks for Subject 1: "))
subject2_marks = float(input("Enter marks for Subject 2: "))
subject3_marks = float(input("Enter marks for Subject 3: "))

total_marks = (subject1_marks+subject2_marks+subject3_marks)
average = (total_marks/3)

print(f"Total marks scored by {name} are:",total_marks)
print(f"Average marks:",average)