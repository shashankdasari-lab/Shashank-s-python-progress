#write a program to check if list contains palindrome
mainlist=[]
list=int(input("enter no 1:"))
mainlist.append(list)
list=int (input("enter no 2:"))
mainlist.append(list)
list=int (input("enter no 3:"))
mainlist.append(list)
list=int (input("enter no 4:"))
mainlist.append(list)
list=int (input("enter no 5:"))
mainlist.append(list)
print(mainlist)
copy=mainlist.copy()
copy.reverse()
print(copy)

if copy == list:
    print("it is palindrome")
else:
    print("Not a palindrome")   


