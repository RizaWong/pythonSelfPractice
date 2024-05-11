# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 20:46:22 2023

@author: Rizalyn
"""
#DICTIONARY TOPIC, example

pets={"Gerald":"dog", "Alyn":"pig", "Talyn":"cat"}
print (pets)

#we can use the .update method if we want to add another items on the dictionary list
pets={"Gerald":"dog", "Alyn":"pig", "Talyn":"cat"}
pets.update({"Ron":"rat", "Paul":"lizard"})
print (pets)

#we can make a dictionary list using DICT and ZIP Function
relative= ["Tita Maloy", "Jeff", "Tito Roger", "Veronica"]
age = [54, 14, 55, 19]

re_age=dict(zip(relative,age))

print(re_age)

#example of checking if a key variable is in the dictionary
exam_scores={"Jonathan": 85, "Anna": 90, "Roza": 98, "Alex": 89, "Jeff":78, "Roger":"60"}

if "Andrew" in exam_scores:
    print ("Andrew, took a test.")
    
else:
    print ("Andrew, didn't take a test.")