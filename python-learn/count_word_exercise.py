#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 20:12:46 2018
@author: praveen
count words in a text file
"""
import sys

in_file =sys.argv[1]
txt = open(in_file)

word_dict={}

for lines in txt:
    for word in lines.split():
        word=word.lower().strip("'?,.;!-/\"")
        if word not in word_dict :
            word_dict[word]=0
        word_dict[word]=word_dict[word]+1
word_list= sorted(word_dict)
for element in word_list:
    print(element,word_dict[element])
txt.close()