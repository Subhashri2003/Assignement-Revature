"""
Program: Slice Characters of User Choice
Description: Takes user start and end indexes and slices the string accordingly.
Displays an error message if the slicing is invalid.
"""

# Input
string = input("Enter the string: ")
start = int(input("Enter start index: "))
end = int(input("Enter end index: "))

# Logic with validation
if 0 <= start < len(string) and 0 < end <= len(string) and start < end:
    print("Sliced string:", string[start:end])
else:
    print("Error: Invalid slice range!")
