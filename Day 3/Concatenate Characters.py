"""
Program: Concatenate Characters of User Choice
Description: Concatenates specific characters (by index) chosen by the user.
Displays error message if any index is invalid.
"""

# Input
string = input("Enter the string: ")
indexes = input("Enter indexes separated by spaces: ")

try:
    indices = [int(i) for i in indexes.split()]
    result = "".join(string[i] for i in indices)
    print("Concatenated result:", result)
except (ValueError, IndexError):
    print("Error: Invalid index entered!")
