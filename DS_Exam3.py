# -*- coding: utf-8 -*-

"""Programming: Estimating the number of primes less than x Write a program to count
 how many primes are less than 10, 100, 1,000, ..., 100,000,000. Fit a curve to your 
 data and estimate the number of primes less than x, where x is a positive integer."""

def is_a_prime_number_basic(number_to_check):
    is_prime = True
    for check_value in range(2, number_to_check):
        if 0 == number_to_check % check_value:
            is_prime = False
            return is_prime
    return is_prime

lower_limit = 2
list_of_upper_limits = [10,100,1000]

for item in list_of_upper_limits:
    prime_number_count = 0
    upper_limit = item
    for number_to_check in range(lower_limit, upper_limit):
        print('checking to see if {number_to_check} is prime.')
        if is_a_prime_number_basic(number_to_check):
            prime_number_count += 1
        print(f"We found a prime: {number_to_check}. ",end ="")
        print(f"We have found {prime_number_count} so far.")
