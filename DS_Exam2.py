# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 13:20:33 2022

@author: matth
"""

# Use the cashier's algorithm. Develop a program that randomly selects a total charge. Then randomly select a payment in dollars and cents that exceeds that charge. Then have the program calculate the change in pennies, nickels, dimes, quarters, ones, fives, and twenties.

import random
Total = round(random.uniform(1, 50), 2)
print("Amount due:", Total)
Payment = round(random.uniform(50, 100), 2)
print("Amount payed:", Payment)

change = Payment - Total
print('Your change is:', change)

Dollars = 0
Quarters = 0
Dimes = 0
Nickels = 0
Pennies = 0

while change >= 1.00:
    Dollars = Dollars + 1
    change = change - 1.00
    
while change >= .01:
    Pennies = Pennies + 1
    change = change - .01
    
while change >= .05:
    Nickels = Nickels + 1
    change = change - .01
    
while change >= .10:
    Dimes = Dimes + 1
    change = change - .10
    
while change >= .25:
    Quarters = Quarters + 1
    change = change - .25

    Nickels = Nickels + 1
    change = change - .0