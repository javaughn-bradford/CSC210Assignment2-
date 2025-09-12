#search.py

# Modified by: javaughn bradford
#linear search
def linear_search(lst, key):
    for item in lst:
        if item == key:
            return True
    return False
#bineary search
def binary_search(data, target):
    low = 0
    high = len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        if data[mid] == target:
            return True
