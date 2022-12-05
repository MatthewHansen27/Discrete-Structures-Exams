# -*- coding: utf-8 -*-

from itertools import combinations_with_replacement
#https://www.geeksforgeeks.org/permutation-and-combination-in-python/

varieties = ["plain", "chocolate", "strawberry"]

print(f"Our varieties are: {varieties}")


# pick 6 donuts from 3 varieties with replacement.
donut_combinations = combinations_with_replacement(varieties, 6)

# Print the obtained combinations 
index = 0
for i in list(donut_combinations): 
    index += 1
    print(f'# {index}: ', end = '')
    print (i) 


