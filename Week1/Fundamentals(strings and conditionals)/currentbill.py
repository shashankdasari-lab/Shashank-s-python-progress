#Electricty bill generator 

name=str(input("Enter your name:"))
units=int(input("enter units consumed:"))

if units>=0 and units<=100:
    print("\nELECTRICITY BILL\n")
    print ("Customer name:",name)
    print(f"5 Rs per unit as {units} have been consumed ")
    print(f"Your current bill for {units} units is ",units*5)

elif units>=101 and units<=200:
    print("\nELECTRICITY BILL\n")
    print ("Customer name:",name)
    print(f"7 Rs per unit as {units} units have been consumed ")
    print(f"Your current bill for {units} units is ",units*7)

elif units>=201 and units<=500:
    print("\nELECTRICITY BILL\n")
    print ("Customer name:",name)
    print(f"10 Rs per unit as {units} have been consumed ")
    print(f"Your current bill for {units} units is ",units*10)

elif units>=501:
    print("\nELECTRICITY BILL\n")
    print ("Customer name:",name)
    print(f"15 Rs per unit as {units} have been consumed ")
    print(f"Your current bill for {units} units is ",units*15)
else:
    print("Enter a valid value")