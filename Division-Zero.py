# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 18:37:51 2023

@author: Rizalyn
"""

num1 = eval (input ('Enter the first number: '))

num2 = eval (input ('Enter the second number: '))

operation = input ("What operation do you want to perform? (=, -, x, /) ")

if operation == '+':
    answer = num1 + num2

elif operation == '-':
    answer = num1 - num2
    
elif operation == 'x':
    answer = num1 * num2
    
elif operation == '/':
    if num2 != 0:
        answer = num1 / num2
    else:
        print("Error: Division by zero.")
        answer = None
        
if answer is not None:
    print(f"The result is {answer}.")