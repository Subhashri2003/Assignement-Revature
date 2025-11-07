"""
Program: Print Duplicates from List
Description: Displays duplicate numbers from a list.
"""

numbers = [1, 2, 3, 2, 4, 5, 6, 5, 2]
duplicates = []

for num in numbers:
    if numbers.count(num) > 1 and num not in duplicates:
        duplicates.append(num)

print("Duplicate elements:", duplicates)
