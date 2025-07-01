import bank

def deposit(accno, amount):
    if accno in bank.accounts:
        bank.accounts[accno][2] += amount
        return True
    else:
        return False

def withdraw(accno, amount):
    if accno in bank.accounts:
        if amount < bank.accounts[accno][2]:
            bank.accounts[accno][2] -= amount
            return 1  # Success
        else:
            return 2  # Insufficient balance
    else:
        return 3  # Account not found

def find_account(accno):
    if accno in bank.accounts:
        return bank.accounts[accno][2]
    else:
        return None
