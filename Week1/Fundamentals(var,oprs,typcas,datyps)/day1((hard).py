#employee payroll System

print("\nWELCOME TO EMPLOYEE PAYROLL SYSTEM\n ")

emp_name=str(input("Enter Employee Name : "))
emp_ID=str(input("Enter Employee ID :"))
emp_dept=str (input("Enter Department:"))

print("\nSALARY DETAILS SECTION\n")

basic_salary=int(input("Enter your basic salary:"))
bonus=int(input("Enter your bonus amount:")) 
deductions=int(input("Enter your deductions:"))

print("\nEMPLOYEE PAYROLL REPORT\n")

print("Employee name:",emp_name)
print("Employee ID:",emp_ID)
print("Employee Department:",emp_dept)

final_salary=(basic_salary+bonus-deductions)

print("\n Final salary : ",final_salary)