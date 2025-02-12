import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pytest
from utils import hash_password, create_account, deposit_to_account, withdraw_from_account
from db_handler import load_accounts, save_accounts
from unittest.mock import mock_open, patch

def test_hash_password():
    password = "12345"
    hashed = hash_password(password)
    assert isinstance(hashed, str)

def test_create_account():
    accounts = {}
    # Anropa create_account med både namn och lösenord
    account_id = create_account(accounts, "Sabrina", "hemligt")
    assert account_id == "1"
    assert accounts[account_id]["name"] == "Sabrina"
    assert accounts[account_id]["balance"] == 0

def test_deposit_to_account():
    accounts = {"1": {"name": "Sabrina", "balance": 100, "password": "hashed_password"}}
    deposit_to_account(accounts, "1", 50)
    assert accounts["1"]["balance"] == 150

def test_withdraw_from_account():
    accounts = {"1": {"name": "Sabrina", "balance": 100, "password": "hashed_password"}}
    result = withdraw_from_account(accounts, "1", 50)
    assert result == True
    assert accounts["1"]["balance"] == 50

def test_invalid_withdraw():
    accounts = {"1": {"name": "Sabrina", "balance": 100, "password": "hashed_password"}}
    result = withdraw_from_account(accounts, "1", 150)
    assert result == False
    assert accounts["1"]["balance"] == 100

@patch("builtins.open", new_callable=mock_open, read_data="account_id,name,balance,password\n1,Sabrina,1000,hashed_password")
def test_load_accounts(mock_file):
    accounts = load_accounts("dummy.csv")
    assert "1" in accounts
    assert accounts["1"]["name"] == "Sabrina"

@patch("builtins.open", new_callable=mock_open)
def test_save_accounts(mock_file):
    accounts = {"1": {"name": "Sabrina", "balance": 1000, "password": "hashed_password"}}
    save_accounts("dummy.csv", accounts)
    mock_file().write.assert_called()
