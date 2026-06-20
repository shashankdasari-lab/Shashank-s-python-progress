marks=[10,20,40,76,33]
print(marks)
print(type(marks))
print(len(marks))
print(marks[3])
marks[0]=44 #it is changble
print(marks)

#list slicing

list1=["dasari",18,98.6,"hyderabad"]
print(list1[0:2])
print(list1[0:])
print(list1[:2])

#list operatios or functions

list2=[5,7,9,4,2,8]
list2.append(99)
print(list2)
list2.sort()
list2.sort(reverse=True)
list2.insert(3,65)
print(list2)    #sorting is possible in strings (alphabetically)
