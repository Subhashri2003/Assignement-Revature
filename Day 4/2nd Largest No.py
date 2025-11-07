"""
Program: Find Second Largest Number in List
Description: Finds the second largest number from a list of numbers.
"""

numbers = [12, 35, 1, 10, 34, 1]
unique_numbers = list(set(numbers))  # Remove duplicates
unique_numbers.sort()

if len(unique_numbers) < 2:
    print("Not enough unique numbers!")
else:
    print("Second largest number is:", unique_numbers[-2])
