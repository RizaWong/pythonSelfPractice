# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 11:49:24 2023

@author: Rizalyn
"""

username = ["Riza12", "Mary20", "Jelly08"]
password =["123456", "789101", "246890"]

user= input ("Enter Username: ")

pw= input ("Enter Password: ")

for i in range (len(username)):
    if user==username[i] and pw==password[i]:
        print ("\nWelcome, " +  username[i] + ".")
        break
else:
    print ("\nAccount Not Found.")