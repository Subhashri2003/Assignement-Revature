"""
Program: Print Floyd's Triangle
Author: Subha Shri
Description:
    Prints Floyd's Triangle for given number of rows.
    The triangle contains consecutive natural numbers
    starting from 1, arranged in a right-angled format.

Input:
    An integer N (number of rows)

Output:
    Floyd's Triangle pattern with N rows
"""

def print_floyds_triangle(rows):
    """Prints Floyd's Triangle up to the given number of rows."""
    num = 1  # starting number
    for i in range(1, rows + 1):
        for j in range(i):
            print(num, end=" ")
            num += 1
        print()  # move to next line after each row


def main():
    rows = int(input("Enter number of rows: "))
    print_floyds_triangle(rows)


if __name__ == "__main__":
    main()
