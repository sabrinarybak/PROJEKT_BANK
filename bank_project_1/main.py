from utils import create_account, list_accounts, deposit_to_account, withdraw_from_account, search_account
from db_handler import load_accounts, save_accounts
from api import convert_currency
import hashlib

# Funktion för att hasha lösenord
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def main():
    print("Välkommen till Bankens Kontoapplikation!")

    # Ladda konton från CSV-fil
    accounts_file = "accounts.csv"
    accounts = load_accounts(accounts_file)

    while True:
        print("""
        Meny:
        1. Skapa konto
        2. Lista alla konton
        3. Insättning
        4. Uttag
        5. Sök efter ett konto
        6. Valutakonvertering
        7. Ta bort ett konto
        8. Avsluta
        """)
        try:
            val = int(input("Välj ett alternativ (1-8): ").strip())
        except ValueError:
            print("❌ Ogiltig inmatning. Ange ett nummer mellan 1 och 8.")
            continue

        if val == 1:
            # Skapa nytt konto
            print("🔹 Skapa nytt konto:")
            namn = input("Ange namn på kontoinnehavaren: ").strip()
            try:
                balans = float(input("Ange startbalans: ").strip())
            except ValueError:
                print("❌ Ogiltigt belopp. Försök igen.")
                continue
            lösenord = input("Ange lösenord för kontot: ").strip()
            hashat_lösenord = hash_password(lösenord)
            
            # Hämta högsta konto-ID och öka med 1
            nytt_konto_id = max(accounts.keys(), default=0) + 1
            accounts[nytt_konto_id] = {
                "name": namn,
                "balance": balans,
                "password": hashat_lösenord
            }
            print(f"✅ Konto skapat med ID: {nytt_konto_id}")
            save_accounts(accounts_file, accounts)

        elif val == 2:
            # Lista konton
            print("📋 Lista över alla konton:")
            for konto_id, info in accounts.items():
                print(f"ID: {konto_id}, Namn: {info['name']}, Saldo: {info['balance']}")

        elif val in [3, 4]:  # Hantera insättning och uttag tillsammans
            try:
                konto_id = int(input("Ange konto-ID: ").strip())
            except ValueError:
                print("❌ Ogiltigt konto-ID. Försök igen.")
                continue

            if konto_id not in accounts:
                print("⚠️ Konto-ID hittades inte.")
                continue

            try:
                belopp = float(input("Ange belopp: ").strip())
            except ValueError:
                print("❌ Ogiltigt belopp. Försök igen.")
                continue

            if val == 3:  # Insättning
                accounts[konto_id]["balance"] += belopp
                print(f"💰 {belopp} har satts in på konto {konto_id}.")
            elif val == 4:  # Uttag
                if belopp <= accounts[konto_id]["balance"]:
                    accounts[konto_id]["balance"] -= belopp
                    print(f"💸 {belopp} har tagits ut från konto {konto_id}.")
                else:
                    print("⚠️ Otillräckligt saldo.")

            save_accounts(accounts_file, accounts)

        elif val == 5:
            # Sök efter konto
            try:
                konto_id = int(input("Ange konto-ID att söka efter: ").strip())
            except ValueError:
                print("❌ Ogiltigt konto-ID. Försök igen.")
                continue

            if konto_id in accounts:
                konto = accounts[konto_id]
                print(f"🔍 ID: {konto_id}, Namn: {konto['name']}, Saldo: {konto['balance']}")
            else:
                print("⚠️ Konto-ID hittades inte.")

        elif val == 6:
            # Valutakonvertering
            try:
                konto_id = int(input("Ange konto-ID för valutakonvertering: ").strip())
            except ValueError:
                print("❌ Ogiltigt konto-ID. Försök igen.")
                continue

            if konto_id in accounts:
                saldo = accounts[konto_id]["balance"]
                print(f"💰 Nuvarande saldo: {saldo}")
                target_currency = input("Ange målets valuta (ex. USD, EUR): ").strip().upper()
                nytt_saldo = convert_currency(saldo, target_currency)
                if nytt_saldo:
                    print(f"✅ Konverterat saldo i {target_currency}: {nytt_saldo}")
                else:
                    print("⚠️ Valutakonvertering misslyckades.")
            else:
                print("⚠️ Konto-ID hittades inte.")

        elif val == 7:
            # Ta bort konto
            try:
                konto_id = int(input("Ange konto-ID att ta bort: ").strip())
            except ValueError:
                print("❌ Ogiltigt konto-ID. Försök igen.")
                continue

            if konto_id in accounts:
                confirmation = input("⚠️ Är du säker på att du vill ta bort detta konto? (j/n): ").strip().lower()
                if confirmation == "j":
                    del accounts[konto_id]
                    print(f"🗑️ Konto {konto_id} har tagits bort.")
                    save_accounts(accounts_file, accounts)
                else:
                    print("❌ Kontot togs inte bort.")
            else:
                print("⚠️ Konto-ID hittades inte.")

        elif val == 8:
            # Avsluta programmet
            print("💾 Sparar data och avslutar...")
            save_accounts(accounts_file, accounts)
            break

        else:
            print("❌ Ogiltigt val, försök igen.")

if __name__ == "__main__":
    main()
