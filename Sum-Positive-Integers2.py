# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 18:26:01 2023

@author: Rizalyn
"""

integers_list=[2,3,4,-5,-6,-8,-9,0]

# every element of the list is associated with an INDEX

total_sum= 0
index=0

while index <len(integers_list):
    if integers_list[index]>0:
        total_sum+=integers_list[index]
    index += 1
    
print (f"The sum of positive integers is: {total_sum}")



