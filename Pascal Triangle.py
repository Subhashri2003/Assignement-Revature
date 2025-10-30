"""
Program: Print Pascal's Triangle
Author: Subha Shri
Description:
    Build and print the first N rows of Pascal's Triangle.
    Each row is generated from the previous row by summing
    adjacent pairs (with implicit zeros at both ends).

Input:
    An integer N (number of rows).

Output:
    Prints N rows of Pascal's Triangle.
"""

def print_pascals_triangle(n_rows):
    """Generate and print n_rows of Pascal's Triangle."""
    if n_rows <= 0:
        return

    row = [1]
    for _ in range(n_rows):
        # print current row
        print(' '.join(str(x) for x in row))
        # build next row by summing adjacent pairs with padding
        next_row = [1]  # every row starts with 1
        for i in range(1, len(row)):
            next_row.append(row[i - 1] + row[i])
        next_row.append(1)  # every row ends with 1
        row = next_row


def main():
    rows = int(input("Enter number of rows: "))
    print_pascals_triangle(rows)


if __name__ == "__main__":
    main()
