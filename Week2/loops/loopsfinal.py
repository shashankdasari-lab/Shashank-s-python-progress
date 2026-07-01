user=(int(input("Enter your bank balance:")))

print(" ATM TRANSACTION SIMULATOR ")

balance = float(input("Enter your initial account balance: "))

while True:

    print("\n ATM MENU ")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        deposit = float(input("Enter deposit amount: "))
        balance += deposit
        print("Amount deposited successfully.")
        print("Updated Balance:", balance)

    elif choice == 2:
        withdraw = float(input("Enter withdrawal amount: "))

        if withdraw <= balance:
            balance -= withdraw
            print("Amount withdrawn successfully.")
            print("Updated Balance:", balance)
        else:
            print("Insufficient Balance!")

    elif choice == 3:
        print("Current Balance:", balance)

    elif choice == 4:
        print("\nThank you for using our ATM.")
        break

    else:
        print("Invalid Choice! Please try again.")