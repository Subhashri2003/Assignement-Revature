"""
Program: Print Anagrams Together
Description: Groups words that are anagrams of each other using dictionary.
"""

words = ["eat", "tea", "tan", "ate", "nat", "bat"]
anagrams = {}

for word in words:
    key = ''.join(sorted(word))
    anagrams.setdefault(key, []).append(word)

print("Anagrams grouped together:")
for group in anagrams.values():
    print(group)
