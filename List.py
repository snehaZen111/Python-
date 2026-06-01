# 1. Create a List

fruits = ["Apple", "Banana", "Mango"]

print(fruits)

# Output:
# ['Apple', 'Banana', 'Mango']

# 2. Access List Elements

fruits = ["Apple", "Banana", "Mango"]

print(fruits[0])
print(fruits[1])

# Output:
# Apple
# Banana

# 3. Negative Indexing

fruits = ["Apple", "Banana", "Mango"]

print(fruits[-1])

# Output:
# Mango

# 4. List Slicing

numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])

# Output:
# [20, 30, 40]

# 5. Add Element using append()

fruits = ["Apple", "Banana"]

fruits.append("Mango")

print(fruits)

# Output:
# ['Apple', 'Banana', 'Mango']

# 6. Insert Element

fruits = ["Apple", "Banana"]

fruits.insert(1, "Orange")

print(fruits)

# Output:
# ['Apple', 'Orange', 'Banana']

# 7. Remove Element

fruits = ["Apple", "Banana", "Mango"]

fruits.remove("Banana")

print(fruits)

# Output:
# ['Apple', 'Mango']

# 8. Pop Element

fruits = ["Apple", "Banana", "Mango"]

fruits.pop()

print(fruits)

# Output:
# ['Apple', 'Banana']

# 9. Length of List

numbers = [10, 20, 30, 40]

print(len(numbers))

# Output:
# 4

# 10. Loop Through List

fruits = ["Apple", "Banana", "Mango"]

for item in fruits:
    print(item)

# Output:
# Apple
# Banana
# Mango

# 11. Check Item in List

fruits = ["Apple", "Banana", "Mango"]

if "Banana" in fruits:
    print("Found")

# Output:
# Found

# 12. Sort List

numbers = [40, 10, 30, 20]

numbers.sort()

print(numbers)

# Output:
# [10, 20, 30, 40]

# 13. Reverse List

numbers = [10, 20, 30, 40]

numbers.reverse()

print(numbers)

# Output:
# [40, 30, 20, 10]

# 14. Copy List

fruits = ["Apple", "Banana"]

new_list = fruits.copy()

print(new_list)

# Output:
# ['Apple', 'Banana']

# 15. Clear List

fruits = ["Apple", "Banana", "Mango"]

fruits.clear()

print(fruits)

# Output:
# []

