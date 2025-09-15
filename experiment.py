# experiment.py
# Run time trials of searching algorithms
# Starter Code from CSC 210
#Javaughn b
# I had chat gpt do some touchups and on my linear and binary equations because they didn't add up 

from random import randint
from search import linear_search, binary_search
from time import perf_counter_ns

# Generate a random list of integers with
# every integer between *min_value* and *max_value*
# of length, *length*
def random_int_list(length, min_value, max_value):
    return [randint(min_value, max_value) for _ in range(length)]
    

def time_trial(num_trials, data_size, min_value, max_value):
    # Initialize accumulators for total time
    total_linear_time = 0
    total_binary_time = 0

    # random data
    data = random_int_list(data_size, min_value, max_value)
    sorted_data = sorted(data)  # Pre-sort for binary search

    #Trials
    for _ in range(num_trials):
        search_key = randint(min_value, max_value)

        #linear search
        start_time = perf_counter_ns()
        linear_search(data, search_key)
        end_time = perf_counter_ns()
        total_linear_time += (end_time - start_time)

        # binary search
        start_time = perf_counter_ns()
        binary_search(sorted_data, search_key)
        end_time = perf_counter_ns()
        total_binary_time += (end_time - start_time)

    # averages
    avg_linear_time = total_linear_time / num_trials
    avg_binary_time = total_binary_time / num_trials

    return avg_linear_time, avg_binary_time
