# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 15:17:21 2023

@author: Rizalyn
"""

def withdraw_money(current_balance, amount):
    if (current_balance >= amount):
        current_balance = current_balance - amount
        return current_balance 
    
balance = withdraw_money (100, 60)

if balance <= 50:
    print ("We need to make a deposit.")
    
else:
    print ("Nothing to see here!")