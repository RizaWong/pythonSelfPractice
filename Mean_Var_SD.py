# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 20:33:52 2023

@author: Rizalyn
"""

import statistics 

dataset=[]

number=eval(input("How many data you want to input?"))

for i in range (number):
    i+=1
    data=eval(input(f"Enter Data {i}: "))
    dataset.append(data)

meanValue = statistics.mean(dataset)

standardDev_sample=statistics.stdev(dataset, xbar=meanValue)

standardDev_population=statistics.pstdev(dataset)

variance=statistics.variance(dataset, xbar=meanValue)

print (f"\nMEAN: {meanValue:.2f}")

print (f"VARIANCE: {variance:.2f}")

print (f"SD OF SAMPLE: {standardDev_sample:.2f}")

print (f"SD OF POPULATION: {standardDev_population:.2f}")

