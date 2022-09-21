# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 15:44:43 2022

@author: matth
"""


from random import random


def generate_sequence(sp):
    
    rule1 = lambda x : x + 1
    rule2 = lambda x : x + 2
    rule3 = lambda x : x + 3
    rule4 = lambda x : x + 4

    rules = [rule1, rule2, rule3, rule4]

   
    random_index = int(random()*4)
    rule = rules[random_index]

    print('Sequence is : ', sp, end=' ')
    for i in range(3):
        sp = rule(sp)
        print(sp, end=' ')

    term = int(input('\nGuess the next term: '))

    if term == rule(sp):
        print('You\'re correct')
    else:
        print('Incorrect! The correct answer is ', rule(sp))

sp = 1
generate_sequence(sp)
