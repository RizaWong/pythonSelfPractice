# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 11:32:25 2023

@author: Rizalyn
"""

import pandas as pd

try:
    excel_file = input('Enter the path of the Excel file: ')
    
    file = pd.read_excel(excel_file)
    print (file.to_string(index=False))
    
except Exception as e:
    print(f"Error: {e}")
