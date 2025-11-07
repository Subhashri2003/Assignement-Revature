"""
Program: Factorial of a Number
Description: Defines a function that calculates and returns the factorial
of a given number using iteration.
"""

def factorial(num):
    """Return the factorial of a given number."""
    if num < 0:
        return "Error: Factorial of negative number not defined."
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return fact

# Input and Output
n = int(input("Enter a number: "))
print("Factorial of", n, "is:", factorial(n))
