# api.py
# (C: API-integration med requests)
import requests

def get_exchange_rate(from_currency, to_currency):
    """
    Hämtar växelkurs från ett API och returnerar den som float.
    """
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if to_currency in data.get("rates", {}):
            return float(data["rates"][to_currency])
        else:
            print("Valutan stöds inte.")
            return None
    except Exception as e:
        print("Ett fel inträffade vid hämtning av växelkurs:", e)
        return None

def convert_currency(amount, rate_or_target):
    """
    Om rate_or_target är en siffra (int/float) görs en direkt multiplikation.
    Om den är en sträng betraktas den som målvaluta och ett API-anrop görs.
    """
    # Om den andra parametern är numerisk, multiplicera direkt.
    if isinstance(rate_or_target, (int, float)):
        return float(amount) * rate_or_target
    else:
        # Annars antar vi att den är en sträng med målvaluta (ex: "USD")
        from_currency = "SEK"  # Du kan ändra detta vid behov
        url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            if rate_or_target in data.get("rates", {}):
                rate = float(data["rates"][rate_or_target])
                return float(amount) * rate
            else:
                print("Valutan stöds inte.")
                return None
        except Exception as e:
            print("Ett fel inträffade vid hämtning av växelkurs:", e)
            return None
