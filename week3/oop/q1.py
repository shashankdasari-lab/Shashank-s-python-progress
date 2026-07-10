class Student:
    def __init__(self,name,a,b):
        self.name=name
        self.sub1=a
        self.sub2=b
        

    def avg(self):
        avge=(self.sub1+self.sub2)/2
        return avge
    
s1=Student("shax",23,24)



print("Your avg:",s1.avg())
