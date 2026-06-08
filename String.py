# 1. String Creation

text = "Hello Python"
print(text)

# Output:
# Hello Python

# 2. String Length

text = "Python"
print(len(text))

# Output:
# 6

# 3. String Reverse

text = "Python"
print(text[::-1])

# Output:
# nohtyP

# 4. Palindrome Check

text = "madam"

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

# Output:
# Palindrome

# 5. Count Vowels

text = "hello"
vowels = "aeiou"
count = 0

for ch in text:
    if ch in vowels:
        count += 1

print(count)

# Output:
# 2

# 6. Uppercase and Lowercase

text = "Python"

print(text.upper())
print(text.lower())

# Output:
# PYTHON
# python

# 7. Replace Character

text = "hello"
print(text.replace("h", "j"))

# Output:
# jello

# 8. Split String

text = "I love Python"
print(text.split())

# Output:
# ['I', 'love', 'Python']

# 9. Find Word Position

text = "I love Python"
print(text.find("love"))

# Output:
# 2

# 10. Loop Through String

text = "ABC"

for ch in text:
    print(ch)

# Output:
# A
# B
# C
