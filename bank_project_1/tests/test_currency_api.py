import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from api import get_exchange_rate, convert_currency
import pytest

def test_get_exchange_rate():
    """
    Testar om vi kan hämta en giltig växelkurs för en given valuta.
    """
    rate = get_exchange_rate("USD", "SEK")
    assert rate is not None, "Växelkursen bör inte vara None"
    assert rate > 0, "Växelkursen bör vara större än 0"
    assert isinstance(rate, float), "Växelkursen bör vara en float"

def test_convert_currency():
    """
    Testar om konverteringsfunktionen returnerar korrekt resultat.
    """
    amount = 100
    rate = 10.5  # Simulerad växelkurs
    converted_amount = convert_currency(amount, rate)
    assert converted_amount == 1050, "Konverteringen bör ge rätt belopp"
    assert isinstance(converted_amount, float), "Resultatet bör vara en float"