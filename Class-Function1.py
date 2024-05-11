# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 20:00:29 2023

@author: Rizalyn
"""
#Creating and Using a Class

class Puppy():
    def __init__(self, name, favorite_toy):
        self.name = name
        self.favorite_toy = favorite_toy
        
    def plaay(self):
        print(self.name + " is playing with the" + self.favorite_toy)

marble = Puppy ("Marble", " teddy bear.")
marble.plaay()

onyx = Puppy ("Onyx", " lizard.")
onyx.plaay()