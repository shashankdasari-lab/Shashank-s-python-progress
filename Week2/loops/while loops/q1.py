#find X elements of following tuple using loop [1,4,9,16,25,36,49,64,81,100]
tple=(1,4,9,16,25,36,49,64,81,100)
x=int (input("Enter a number to find :"))
i=0
while i < (len(tple)):
    if (tple[i]==x):
        print("number found at index:",i)
        break
    else :
        print("number not found ")
    i += 1