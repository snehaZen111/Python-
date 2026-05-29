# 1. Create a Tuple

fruits = ("Apple", "Banana", "Mango")

print(fruits)

# Output:
# ('Apple', 'Banana', 'Mango')

# 2. Access Tuple Elements

fruits = ("Apple", "Banana", "Mango")

print(fruits[0])
print(fruits[1])

# Output:
# Apple
# Banana

# 3. Negative Indexing in Tuple

fruits = ("Apple", "Banana", "Mango")

print(fruits[-1])

# Output:
# Mango

# 4. Tuple Slicing

numbers = (10, 20, 30, 40, 50)

print(numbers[1:4])

# Output:
# (20, 30, 40)

# 5. Length of Tuple

numbers = (10, 20, 30, 40)

print(len(numbers))

# Output:
# 4

# 6. Loop Through Tuple

colors = ("Red", "Blue", "Green")

for i in colors:
    print(i)

# Output:
# Red
# Blue
# Green

# 7. Check Item in Tuple

fruits = ("Apple", "Banana", "Mango")

if "Banana" in fruits:
    print("Found")

# Output:
# Found

# 8. Count Method in Tuple

numbers = (1, 2, 3, 2, 2, 4)

print(numbers.count(2))

# Output:
# 3

# 9. Index Method in Tuple

numbers = (10, 20, 30, 40)

print(numbers.index(30))

# Output:
# 2

# 10. Convert Tuple to List

fruits = ("Apple", "Banana", "Mango")

x = list(fruits)

print(x)

# Output:
# ['Apple', 'Banana', 'Mango']

