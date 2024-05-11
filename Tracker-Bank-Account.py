# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 19:27:35 2023

@author: Rizalyn
"""

# Initialize an empty dictionary to store account information
accounts = {}

# Function to create a new account
def create_account(account_number, initial_balance):
    accounts[account_number] = initial_balance
    print(f"Account {account_number} created with initial balance of {initial_balance}")

# Function to look up an existing account
def lookup_account(account_number):
    if account_number in accounts:
        return accounts[account_number]
    else:
        print(f"Account {account_number} not found")

# Function to deposit money into an existing account
def deposit(account_number, amount):
    if account_number in accounts:
        accounts[account_number] += amount
        print(f"Deposited {amount} into account {account_number}. New balance: {accounts[account_number]}")
    else:
        print(f"Account {account_number} not found")

# Function to withdraw money from an existing account
def withdraw(account_number, amount):
    if account_number in accounts:
        if accounts[account_number] >= amount:
            accounts[account_number] -= amount
            print(f"Withdrew {amount} from account {account_number}. New balance: {accounts[account_number]}")
        else:
            print(f"Insufficient balance in account {account_number}")
    else:
        print(f"Account {account_number} not found")

# Function to print out a list of all accounts and their balances
def print_accounts():
    print("List of all accounts:")
    for account_number, balance in accounts.items():
        print(f"Account {account_number}: Balance {balance}")

# Example usage of the functions
create_account(1001, 5000)
create_account(1002, 10000)
deposit(1001, 2500)
withdraw(1002, 5000)
print_accounts()
