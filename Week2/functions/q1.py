#waf to print len of a list 
def len_list(list):
    b=len(list)
    print("length of list:",b)
    return b
list1=[]
a=(input("enter a element in a list:"))
list1.append(a)
a=(input("enter a element in a list:"))
list1.append(a)
a=(input("enter a element in a list:"))
list1.append(a)

print("Your list:",list1)


len_list(list1)

