# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 12:37:34 2023

@author: Rizalyn
"""

import re

five_digit_zip = "98101"
nine_digit_zip = "98101-003"
phone_number = "23a-567-8901"

five_digit_expression = r'\d{3}'
print (re.search(five_digit_expression, five_digit_zip))
print (re.search(five_digit_expression, nine_digit_zip))
print (re.search(five_digit_expression, phone_number))