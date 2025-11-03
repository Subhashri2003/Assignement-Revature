"""
Program: Remove Duplicates from String
Description: Removes duplicate characters while preserving order.
"""

# Input
string = input("Enter the string: ")

# Logic using set()
result = ""
for ch in string:
    if ch not in result:
        result += ch

# Output
print("String after removing duplicates:", result)
