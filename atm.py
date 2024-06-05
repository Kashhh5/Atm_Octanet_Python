import time
print("Welcome to ATM ")
print("Please insert your card")
transaction_history = [] 
time.sleep(5)

password=1234                                                                           
balance = 5000

pin = int(input("Enter your PIN: "))
while True:
    if pin == password:
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. Transaction History")
        print("6. Exit")

        option = input("Enter your choice (1-6): ")

        if option == "1":
            print(f"Your balance is: ${balance}")
        elif option == "2":
            amount = float(input("Enter amount to deposit: $"))
            balance += amount
            transaction_history.append(f"Deposited: ${amount}")
            print(f"${amount} deposited successfully!")
        elif option == "3":
            amount = float(input("Enter amount to withdraw: $"))
            if amount > balance:
                print("Insufficient funds!")
            else:
                balance -= amount
                transaction_history.append(f"Withdrew: ${amount}")
                print(f"${amount} withdrawn successfully!")
        elif option == "4":
            amount = float(input("Enter amount to transfer: $"))
            if amount > balance:
                print("Insufficient funds!")
            else:
                recipient = input("Enter recipient's name: ")
                balance -= amount
                transaction_history.append(f"Transferred: ${amount} to {recipient}")
                print(f"${amount} transferred to {recipient} successfully!")
        elif option == "5":
            print("\nTransaction History:")
            for transaction in transaction_history:
                print(transaction)
        elif option == "6":
            print("Thank you for using the ATM!")
            break
        else:
            print("Invalid option! Please select again.")
    else:
        print("Incorrect PIN. Please try again.")