import bank

def create_account(accno, cname, address, balance):
    if accno not in bank.accounts:
        bank.accounts[accno] = [cname, address, balance]
        return True
    else:
        return False

def update_account(accno, address):
    if accno in bank.accounts:
        bank.accounts[accno][1] = address
        return True
    else:
        return False

def delete_account(accno):
    if accno in bank.accounts:
        del bank.accounts[accno]
        return True
    else:
        return False
