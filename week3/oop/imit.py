class Student:
    
    def __init__(self):   ###default constructor
        
        pass

    def __init__(self,fullname,marks): ###parameterized constructor
        self.name=fullname
        self.marks=marks
        print("adding student")

s1=Student("arjun",97)

print(s1.name,s1.marks)

s2=Student("karan",88)
print(s2.name,s2.marks)
