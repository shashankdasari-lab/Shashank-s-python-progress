"""search for number x in tuple using loop """

tple1=(1,4,9,16,25,36,49,64,81,100,1)
user=(int(input("Enter a number:")))
idx=0
for val in tple1:
    if user==val:
        print("number found at index:",idx)
        break
    idx+=1
   