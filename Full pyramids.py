"""
Program: Print Full Pyramid Pattern
Author: Subha Shri
Description:
    This program prints a full pyramid pattern of stars (*)
    based on the number of rows entered by the user.

Input:
    An integer representing the number of rows.

Output:
    A full pyramid pattern displayed on the screen.
"""

rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):
    spaces = " " * (rows - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars)

