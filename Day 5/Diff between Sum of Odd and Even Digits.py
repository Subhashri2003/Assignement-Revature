"""
Program: Difference Between Sum of Odd and Even Digits
Description: Calculates the difference between the sum of odd digits
and even digits in a given number.
"""

# Input
num = input("Enter a number: ")

sum_even = 0
sum_odd = 0

# Logic
for digit in num:
    if digit.isdigit():
        d = int(digit)
        if d % 2 == 0:
            sum_even += d
        else:
            sum_odd += d

difference = abs(sum_odd - sum_even)

# Output
print("Sum of odd digits:", sum_odd)
print("Sum of even digits:", sum_even)
print("Difference:", difference)
