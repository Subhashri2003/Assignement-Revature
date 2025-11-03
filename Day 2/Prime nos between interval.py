"""
Program: Print Prime Numbers in an Interval
Author: Subha Shri
Description:
    This program prints all prime numbers between
    a given start and end range.

Input:
    Two integers - start and end values.

Output:
    Displays prime numbers in that range.
"""

start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

print(f"Prime numbers between {start} and {end} are:")

for num in range(start, end + 1):
    if num > 1:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            print(num)
