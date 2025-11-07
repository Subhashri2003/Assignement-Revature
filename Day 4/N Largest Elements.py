"""
Program: Find N Largest Elements
Description: Finds N largest numbers in a list.
"""

numbers = [4, 5, 1, 2, 9, 7, 10, 8]
n = int(input("Enter N: "))

if n <= len(numbers):
    largest = sorted(numbers, reverse=True)[:n]
    print(f"{n} largest elements are:", largest)
else:
    print("Error: N is greater than list size.")
