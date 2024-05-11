# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 13:49:05 2023

@author: Rizalyn
"""
#CHALLENGE 4 IN SOFTWARE DEVELOPMENT SERIES 3

# PROBLEM: DEBUGGING
problem = """
    def plant_recommendation(care):
    if care = 'low':
        print('aloe')
    elif care == 'medium':
        print('pothos')
    elif care == 'medium':
        print('orchid')

plant_rec('low')
plant_recommendation('medium')
plant_recommendation('high')
"""

# SOLUTION

def plant_recommendation(care):
    if care == 'low':
        print('aloe')
    elif care == 'medium':
        print('pothos')
    elif care == 'high':
        print('orchid')

plant_recommendation('low')
plant_recommendation('medium')
plant_recommendation('high')

