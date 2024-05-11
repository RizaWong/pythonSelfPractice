# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 15:32:26 2023

@author: Rizalyn
"""

class Fruit():
    
    def __init__(self, color):
        self.color = color
        
    def describe(self):
        print (self.color)
Apple = Fruit ("red")
Fruit.describe(Apple)
    