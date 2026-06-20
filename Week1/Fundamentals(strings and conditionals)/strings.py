#concatenation
s1="doeramon"
s2="nobita"
final=s1+ " " +s2
print(final) 
print(len(final)) 

# indexing
s1="hello"
j1=s1[0]
print(j1)

#slicing 

s1="hello"
print(s1[1:4])
print(s1[:4])  # starting index not given so automatically starts from 0
print (s1[1:]) # ending index not given so automatically takes thge final index

#string functions

s1= "hello my name is shashank"
print(s1.endswith("nk"))
print(s1.capitalize())
print(s1.replace("hello","hi"))
print(s1.find("my")) 
print(s1.count("sh"))

#wap to input users first name and print its length

name=str(input("Enter your name:"))
print(len(name))

#wap to find occurance of $in a string

str1="hello my password is 1Shashank$$$"
print(str1.count("$"))