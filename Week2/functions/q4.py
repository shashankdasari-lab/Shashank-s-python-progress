#waf to convert usd to inr

def usd_to_inr(a,b=95.15):
    c=a*b
    print(c)
    return (c)

money=int(input("enter Total USD:"))

usd_to_inr(money)