# 1. Create a Set

fruits = {"Apple", "Banana", "Mango"}

print(fruits)

# Output:
# {'Apple', 'Banana', 'Mango'}


---

# 2. Add Element to Set

fruits = {"Apple", "Banana"}

fruits.add("Mango")

print(fruits)

# Output:
# {'Apple', 'Banana', 'Mango'}


---

# 3. Remove Element from Set

fruits = {"Apple", "Banana", "Mango"}

fruits.remove("Banana")

print(fruits)

# Output:
# {'Apple', 'Mango'}


---

# 4. Loop Through Set

fruits = {"Apple", "Banana", "Mango"}

for item in fruits:
    print(item)

# Output:
# Apple
# Banana
# Mango


---

# 5. Check Element in Set

fruits = {"Apple", "Banana", "Mango"}

if "Banana" in fruits:
    print("Found")

# Output:
# Found


---

# 6. Union of Two Sets

A = {1, 2, 3}
B = {3, 4, 5}

print(A.union(B))

# Output:
# {1, 2, 3, 4, 5}


---

# 7. Intersection of Two Sets

A = {1, 2, 3}
B = {2, 3, 4}

print(A.intersection(B))

# Output:
# {2, 3}


---

# 8. Difference of Two Sets

A = {1, 2, 3}
B = {2, 3, 4}

print(A.difference(B))

# Output:
# {1}


---

# 9. Length of Set

numbers = {10, 20, 30, 40}

print(len(numbers))

# Output:
# 4


---

# 10. Clear Set

fruits = {"Apple", "Banana", "Mango"}

fruits.clear()

print(fruits)

# Output:
# set()


# Duplicate Values in Set

numbers = {1, 2, 2, 3, 3, 4}

print(numbers)

# Output:
# {1, 2, 3, 4}
