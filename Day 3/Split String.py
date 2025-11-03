"""
Program: Split String into Equal Parts
Description: This program splits a string into 'n' equal parts given by the user.
If the string length is not perfectly divisible, it displays an error message.
"""

# Input
string = input("Enter the string: ")
n = int(input("Enter number of equal parts: "))

# Logic
length = len(string)
if length % n != 0:
    print("Error: String cannot be divided equally into", n, "parts.")
else:
    part_size = length // n
    print("The equal parts are:")
    for i in range(0, length, part_size):
        print(string[i:i + part_size])
