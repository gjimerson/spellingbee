import csv
from tkinter import W
from turtle import pos
from flask import Flask

words_file = open('words_alpha.txt', 'r')
words = []
for word in words_file:
        words.append(str(word).lower()[:-1])

def solve_spelling_bee(letters_list, center_letter):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
                'u', 'v', 'w', 'x', 'y', 'z']
    
    forbidden = [l for l in alphabet if l not in letters_list]
    possible = []
    
    for word in words:
        if center_letter in word:
            if word not in possible:
                if len(word) > 3:
                    if any(l in forbidden for l in word) == False:
                        possible.append(word)
                        
    return possible

letters_list = ['t', 'h', 'u', 'g', 'o', 'l', 'a']
center_letter = 'a'
print(solve_spelling_bee(letters_list, center_letter))