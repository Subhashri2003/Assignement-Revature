"""
Program: Merge Two Dictionaries
Description: Combines two dictionaries into one.
"""

dict1 = {'a': 10, 'b': 20}
dict2 = {'c': 30, 'd': 40}

merged = dict1 | dict2  # Python 3.9+
print("Merged dictionary:", merged)
