#waf to find factorial of nj 

def fact_No(n):
    
    mul=1
    for i in range(1,n+1):
        mul*=i
        print(mul)

    return

n=int(input("Enter a number:"))

fact_No(n)