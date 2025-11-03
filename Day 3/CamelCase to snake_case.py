"""
Program: Convert CamelCase to snake_case
Description: Converts a CamelCase string into snake_case format.
"""

# Input
camel = input("Enter a CamelCase string: ")

# Logic
snake = ""
for ch in camel:
    if ch.isupper():
        snake += "_" + ch.lower()
    else:
        snake += ch

# Remove leading underscore if any
if snake.startswith("_"):
    snake = snake[1:]

# Output
print("snake_case string:", snake)
