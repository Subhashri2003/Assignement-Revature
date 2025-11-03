"""
Program: Count the Number of Vowels in a String
Author: Subha Shri
Description:
    This program takes a string from the user and counts
    how many vowels (a, e, i, o, u) are present in it.

Input:
    A string from the user.

Output:
    Displays the total number of vowels in the string.
"""


text = input("Enter a string: ").lower()
vowels = "aeiou"
count = 0

for v in vowels:
    count += text.count(v)

print("Number of vowels:", count)
