import hashlib

def hash_password(password):
    """
    Hashar ett lösenord med SHA256 för säker lagring (A: Säker programmering).
    """
    return hashlib.sha256(password.encode()).hexdigest()

def create_account(accounts, name, password):
    """
    Skapar ett nytt konto med lösenord.
    """
    account_id = str(len(accounts) + 1)
    accounts[account_id] = {
        "name": name,
        "balance": 0,
        "password": hash_password(password)
    }
    return account_id

def list_accounts(accounts):
    """
    Visar alla konton i systemet.
    """
    if accounts:
        for account_id, details in accounts.items():
            print(f"Konto-ID: {account_id}, Namn: {details['name']}, Saldo: {details['balance']} kr")
    else:
        print("Inga konton finns.")

def deposit_to_account(accounts, account_id, amount):
    """
    Gör en insättning på ett konto.
    """
    if account_id in accounts:
        if amount > 0:
            accounts[account_id]["balance"] += amount
            print(f"{amount} kr insatt på konto {account_id}. Nytt saldo: {accounts[account_id]['balance']} kr")
        else:
            print("Beloppet måste vara positivt!")
    else:
        print("Konto-ID hittades inte.") 

def withdraw_from_account(accounts, account_id, amount):
    """
    Gör ett uttag från ett konto.
    Returnerar True om uttaget lyckas, annars False.
    """
    if account_id in accounts:
        if 0 < amount <= accounts[account_id]["balance"]:
            accounts[account_id]["balance"] -= amount
            print(f"{amount} kr uttaget från konto {account_id}. Nytt saldo: {accounts[account_id]['balance']} kr")
            return True
        else:
            print("Otillräckligt saldo eller ogiltigt belopp.")
            return False
    else:
        print("Konto-ID hittades inte.")
        return False

def search_account(accounts, name):
    """
    Söker efter ett konto med angivet namn.
    """
    found = False
    for account_id, details in accounts.items():
        if details["name"].lower() == name.lower():
            print(f"Hittade konto: Konto-ID: {account_id}, Namn: {details['name']}, Saldo: {details['balance']} kr")
            found = True
    if not found:
        print("Inget konto hittades med det namnet.")

