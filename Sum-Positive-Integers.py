# -*- coding: utf-8 -*-
"""
Created on Sat May 11 15:00:44 2024

@author: Rizalyn
"""

num_list=[]

total=0
index=0

times=int(input("How many integers would you like to enter? "))

for i in range (times):
    i+=1
    integer=eval(input(f"Integer {i}: "))
    num_list.append(integer)
    
    
    
while index<len(num_list):
    if num_list[index]>0:
        total+=num_list[index]
    index+=1

print (f"The sum of positive integers is: {total}")