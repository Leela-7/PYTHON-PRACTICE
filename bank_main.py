import bank

print("Simple Banking System")

while True:
    print("1. Create Account")
    print("2. Update Account")
    print("3. Delete Account")
    print("4. Deposit Amount")
    print("5. Withdraw Amount")
    print("6. Check Balance")
    print("7. Exit")
    
    option = int(input("Enter your choice: "))
    
    if option == 1:
        accno = int(input("Enter Account Number: "))
        name = input("Enter Customer Name: ")
        address = input("Enter Address: ")
        balance = float(input("Enter Balance: "))
        b = bank.create_account(accno, name, address, balance)
        if b:
            print("Account Created")
        else:
            print("Account Not Created")
    
    elif option == 2:
        accno = int(input("Enter Account Number: "))
        address = input("Enter Address: ")
        b = bank.update_account(accno, address)
        if b:
            print("Account Updated")
        else:
            print("Account Not Updated")
    
    elif option == 3:
        accno = int(input("Enter Account Number: "))
        b = bank.delete_account(accno)
        if b:
            print("Account Deleted")
        else:
            print("Account Not Deleted")
    
    elif option == 4:
        accno = int(input("Enter Account Number: "))
        amount = float(input("Enter Amount: "))
        b = bank.deposit(accno, amount)
        if b:
            print("Deposit Successful")
        else:
            print("Deposit Failed")
    
    elif option == 5:
        accno = int(input("Enter Account Number: "))
        amount = float(input("Enter Amount: "))
        b = bank.withdraw(accno, amount)
        if b == 1:
            print("Withdraw Successful")
        elif b == 2:
            print("Insufficient Amount")
        elif b == 3:
            print("Invalid Account Number")
    
    elif option == 6:
        accno = int(input("Enter Account Number: "))
        balance = bank.find_account(accno)
        if balance is not None:
            print(f"Balance is {balance}")
        else:
            print("Account Not Found")
    
    elif option == 7:
        break
