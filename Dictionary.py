# 1. Create a Dictionary

student = {
    "name": "Sneha",
    "age": 21,
    "course": "MSc IT"
}

print(student)

# Output:
# {'name': 'Sneha', 'age': 21, 'course': 'MSc IT'}

# 2. Access Dictionary Values

student = {
    "name": "Sneha",
    "age": 21
}

print(student["name"])
print(student["age"])

# Output:
# Sneha
# 21

# 3. Using get() Method

student = {
    "name": "Sneha",
    "age": 21
}

print(student.get("name"))

# Output:
# Sneha

# 4. Change Dictionary Value

student = {
    "name": "Sneha",
    "age": 21
}

student["age"] = 22

print(student)

# Output:
# {'name': 'Sneha', 'age': 22}

# 5. Add New Item in Dictionary

student = {
    "name": "Sneha"
}

student["course"] = "MSc IT"

print(student)

# Output:
# {'name': 'Sneha', 'course': 'MSc IT'}

# 6. Remove Item using pop()

student = {
    "name": "Sneha",
    "age": 21
}

student.pop("age")

print(student)

# Output:
# {'name': 'Sneha'}

# 7. Loop Through Dictionary

student = {
    "name": "Sneha",
    "age": 21
}

for key, value in student.items():
    print(key, ":", value)

# Output:
# name : Sneha
# age : 21

# 8. Dictionary Keys

student = {
    "name": "Sneha",
    "age": 21
}

print(student.keys())

# Output:
# dict_keys(['name', 'age'])

# 9. Dictionary Values

student = {
    "name": "Sneha",
    "age": 21
}

print(student.values())

# Output:
# dict_values(['Sneha', 21])

# 10. Clear Dictionary

student = {
    "name": "Sneha",
    "age": 21
}

student.clear()

print(student)

# Output:
# {}

