"""
Program: Check Whether a String is Palindrome or Not
Author: Subha Shri
Description:
    This program checks if the given string reads
    the same backward as forward.

Input:
    A string from the user.

Output:
    Displays whether the string is a palindrome or not.
"""

text = input("Enter a string: ")

if text == text[::-1]:
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")
