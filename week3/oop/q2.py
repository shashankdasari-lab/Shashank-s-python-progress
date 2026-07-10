class Account:
    def __init__(self,balance,accno):
        self.balance=balance
        self.account=accno
    def deb(self,amount):
        self.balance-=amount
        print(f"Rs {amount} debited")
    def cre(self,amount):
        self.balance+=amount
        print(f"Rs {amount} credited")
    def bal(self):
        return self.balance
        
       
        

acc1=Account(2860,5678)
print(acc1.balance)
print(acc1.account)
acc1.deb(1000)
acc1.cre(500) 
print(acc1.bal() )

