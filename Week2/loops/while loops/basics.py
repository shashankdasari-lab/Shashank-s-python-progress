
#print nos from 1 to 5

i=5
while i>=1:
    print(i)
    i-=1

#print nos from 1 to 100
print("nos from 1 to 100")
i=1
while i<=100:
    print(i)
    i+=1

#print nos from 100 to 1
print("nos from 100 to 1")
i=100
while i>=1:
    print(i)
    i-=1

#multiplication table of n
i=1
num=int(input("Enter a number :"))
while i<=10:
    print(f"{num} X {i} =" ,num*i)
    i+=1

#print elements of following list using loop [1,4,9,16,25,36,49,64,81,100]
list1=[1,4,9,16,25,36,49,64,81,100]

idx=0
i=1
while idx<=len(list1)-1:
   
    print(list1[idx])
    idx+=1



