"""
Program: Check for Consecutive 0's in Binary
Description: Checks whether the binary representation of a number
contains consecutive zeros.
"""

# Input
n = int(input("Enter a number: "))

# Convert to binary string (without '0b')
binary = bin(n)[2:]
print("Binary representation:", binary)

# Logic
if "00" in binary:
    print("Yes, the number has consecutive 0's.")
else:
    print("No, the number does not have consecutive 0's.")
