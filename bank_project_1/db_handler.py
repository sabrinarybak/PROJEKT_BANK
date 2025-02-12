# db_handler.py
import pandas as pd
import os

def load_accounts(accounts_csv):
    try:
        df = pd.read_csv(accounts_csv)

        # Kontrollera att nödvändiga kolumner finns
        required_columns = {"account_id", "name", "balance", "password"}
        if not required_columns.issubset(df.columns):
            raise ValueError(f"Filen saknar nödvändiga kolumner: {required_columns - set(df.columns)}")

        # Konvertera account_id till heltal och balance till float
        df["account_id"] = df["account_id"].astype(int)  # 🔹 Konverterar till int
        df["balance"] = df["balance"].astype(float)  # 🔹 Konverterar till float

        # Omvandla dataframe till en dictionary och säkerställ att nycklarna är int
        accounts = df.set_index("account_id").T.to_dict()
        accounts = {int(k): v for k, v in accounts.items()}  # 🔹 Konvertera nycklar till int
        return accounts

    except FileNotFoundError:
        print(f"⚠️ Filen {accounts_csv} hittades inte. En ny fil kommer att skapas.")
        return {}

    except ValueError as e:
        print(f"🚨 Fel vid läsning av filen: {e}")
        return {}

    except Exception as e:
        print(f"❌ Ett oväntat fel inträffade: {e}")
        return {}

def save_accounts(accounts_csv, accounts):
    try:
        df = pd.DataFrame.from_dict(accounts, orient="index")
        df.index.name = "account_id"  # 🔹 Sätter indexkolumnen som "account_id"
        
        # Se till att rätt datatyper sparas
        df = df.astype({"balance": float})  # 🔹 Balans sparas alltid som float
        df.to_csv(accounts_csv)  # 🔹 Sparar till CSV utan onödigt index
        print(f"✅ Konton sparades framgångsrikt till {accounts_csv}")

    except Exception as e:
        print(f"❌ Fel vid sparande till fil: {e}")
