"""
Program: Extract Digits from Tuple List
Description: Extracts all digits from a list of tuples containing numbers.
"""

tuple_list = [(123, 456), (789, 12), (34, 5)]
digits = [int(d) for tup in tuple_list for num in tup for d in str(num)]
print("Extracted digits:", digits)
