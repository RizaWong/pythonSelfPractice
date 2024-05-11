# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 12:54:44 2023

@author: Rizalyn
"""
#CHALLENGE 4 IN SOFTWARE DEVELOPMENT SERIES 3

# PROBLEM
# kilometers_value = miles_value = 1.6609344
# Take the value entered by a user.
# Convert it to a value in kilometers.
# Print the result to the terminal with the:
# Text description and string concatenation

# SOLUTION
miles = input ("Enter a distance in miles: ")

miles_float = float(miles)
kilometers = miles_float * 1.609344
kilometers_str = str(kilometers)

print ("The Converted Value is " + kilometers_str + ".")

