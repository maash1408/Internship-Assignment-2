# ATM Simulation Program

# Initial balance
initial_balance = 10000  

MIN_BALANCE = 500

while True:
    print("=== ATM SIMULATOR ===")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        print("Current Balance: ₹", initial_balance)

    elif choice == "2":
        amount = float(input("Enter amount to deposit: "))
        if amount > 0:
            initial_balance += amount
            print("Deposit successful!")
            print("New balance: ₹", initial_balance)
        else:
            print("Invalid deposit amount.")

    elif choice == "3":
        amount = float(input("Enter amount to withdraw: "))
        if amount <= 0:
            print("Invalid withdrawal amount.")
        elif amount > initial_balance:
            print("Insufficient balance!")
        elif initial_balance - amount < MIN_BALANCE:
            print("Cannot withdraw! Minimum balance of ₹", MIN_BALANCE, "must be maintained.")
        else:
            initial_balance -= amount
            print("Withdrawal successful!")
            print("New balance: ₹", initial_balance)

    elif choice == "4":
        print("Thank you for using the ATM. Goodbye!")
        break

    else:
        print("Invalid choice! Please select 1-4.")