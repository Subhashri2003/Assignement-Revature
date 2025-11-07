"""
Program: Print Odd Numbers in List
Description: Prints all odd numbers from a given list.
"""

numbers = [10, 21, 4, 45, 66, 93]
odds = [num for num in numbers if num % 2 != 0]
print("Odd numbers:", odds)
