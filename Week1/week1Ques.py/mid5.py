'''5. Student Grade Manager ⭐⭐
Problem Statement

Store marks of 5 subjects in a list.

Generate
Total Marks
Average Marks
Grade'''
print("ENTER MARKS OUT OF 100")
mainlist=[]
marks=int(input("enter marks subject 1:"))
mainlist.append(marks)
marks=int(input("enter marks subject 2:"))
mainlist.append(marks)
marks=int(input("enter marks subject 3:"))
mainlist.append(marks)
marks=int(input("enter marks subject 4:"))
mainlist.append(marks)
marks=int(input("enter marks subject 2:"))
mainlist.append(marks)

total=sum(mainlist)
print("total",total)
avg=(total/5)
percentage=(total/500)*100
if percentage<=100 and percentage>=90:
    print("Grade:A")
elif percentage<=89 and percentage>=80:
    print("Grade B")
elif percentage<=79 and percentage>=60:
    print("Grade C")
elif percentage<=59 and percentage>=50:
    print("Grade D")
else: 
    print("FAIL")

