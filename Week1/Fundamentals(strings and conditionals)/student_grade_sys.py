#student grade system

marks=int(input("Enter your marks out of 100 :"))

if marks >= 90 and marks <=100 :
    print("GRADE A")
elif marks >= 80 and marks <=89 :
    print("GRADE B")
elif marks >= 70 and marks <=79:
    print("GRADE C")
elif marks >=45 and marks <=69:
    print("GRADE D")
elif marks >100 :
    print("Enter marks within 100")
else:
    print("FAIL")