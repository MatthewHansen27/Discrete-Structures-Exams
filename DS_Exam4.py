# -*- coding: utf-8 -*-
"""
Compare the number of operations and the time needed
to compute Fibonacci numbers recursively versus that
needed to compute them iteratively
"""
class Data_tracker:
    # DATA
    def __init__(self):
        self.number_of_times_function_called = 0
        self.if_count = 0
        self.add_count = 0
        self.subtract_count = 0
        self.start_time = 0
        self.stop_time = 0
        self.assignment_count = 0
    # BEHAVIOR
    def increment_assignment_count(self):
        self.assignment_count += 1
    def increment_function_call_count(self):
        self.number_of_times_function_called += 1
    def increment_if_count(self):
        self.if_count += 1
    def increment_add_count(self):
        self.add_count += 1
    def increment_subtract_count(self):
        self.subtract_count += 1
    def print_function_data(self):
        print(f'we called this function {self.number_of_times_function_called} times.')
        print(f'we added {self.add_count} times.')
        print(f'we subtracted {self.subtract_count} times.')
        print(f'we did a if statement {self.if_count} times.')
        print(f'we did an assignment operation {self.assignment_count} times.')
        print("--- %s seconds ---" % (self.stop_time - self.start_time))
# recursive work
# Python program to display the Fibonacci sequence
def recur_fibo(n, recursive_data):
    recursive_data.increment_function_call_count()
    recursive_data.increment_if_count()
    if n <= 1:
        return n
    else:
        recursive_data.increment_add_count()
        recursive_data.increment_subtract_count()
        recursive_data.increment_subtract_count()
        return(recur_fibo(n-1, recursive_data) + recur_fibo(n-2, recursive_data))
import time
recursive_data = Data_tracker()
number_of_terms = int(input('how many terms would you like?'))

