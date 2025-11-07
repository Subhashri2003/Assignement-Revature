"""
Program: List Slicing and Appending Elements
Description: Demonstrates list slicing and appending new elements in Python.
"""

# Creating a list
my_list = [10, 20, 30, 40, 50, 60]

# Slicing
print("Original list:", my_list)
print("First three elements:", my_list[:3])
print("Last three elements:", my_list[-3:])

# Appending new elements
my_list.append(70)
my_list.append(80)
print("List after appending:", my_list)
