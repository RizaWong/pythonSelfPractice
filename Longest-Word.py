# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 18:57:05 2023

@author: Rizalyn
"""

def find_longest_word(words):
    longest_word = ""
    max_length = 0
    for word in words:
        if len(word) > max_length:
            longest_word = word
            max_length = len(word)
    return longest_word

words = ['apple', 'banana', 'pear', 'kiwi']
longest_word = find_longest_word(words)
print(longest_word) 

# Output: 'banana'
