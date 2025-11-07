"""
Program: Remove Duplicate Words from Sentence
Description: Removes repeated words while keeping order intact.
"""

sentence = input("Enter a sentence: ")
words = sentence.split()
unique_words = []

for w in words:
    if w not in unique_words:
        unique_words.append(w)

print("Sentence after removing duplicates:", ' '.join(unique_words))
