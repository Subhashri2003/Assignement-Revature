"""
Program: Sort Dictionary by Key and Value
Description: Demonstrates sorting of a dictionary by its keys and values.
"""

data = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}

# Sort by keys
sorted_by_key = dict(sorted(data.items()))
print("Sorted by keys:", sorted_by_key)

# Sort by values
sorted_by_value = dict(sorted(data.items(), key=lambda x: x[1]))
print("Sorted by values:", sorted_by_value)
