"""
Program: Swap First and Last Characters
Description: Swaps the first and last characters of a given string.
"""

# Input
string = input("Enter the string: ")

# Logic
if len(string) < 2:
    print("Error: String too short to swap.")
else:
    swapped = string[-1] + string[1:-1] + string[0]
    print("String after swapping:", swapped)
