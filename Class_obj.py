# 1. Simple Class and Object

class Student:
    name = "Sneha"

obj = Student()

print(obj.name)

# Output:
# Sneha



# 2. Class with Multiple Objects

class Student:
    name = "Unknown"

obj1 = Student()
obj2 = Student()

obj1.name = "Asha"
obj2.name = "Riya"

print(obj1.name)
print(obj2.name)

# Output:
# Asha
# Riya



# 3. Class with Constructor (__init__)

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

obj = Student("Sneha", 21)

print(obj.name)
print(obj.age)

# Output:
# Sneha
# 21



# 4. Class with Method

class Student:
    def __init__(self, name):
        self.name = name

    def show(self):
        print("Name is", self.name)

obj = Student("Sneha")
obj.show()

# Output:
# Name is Sneha


# 5. Multiple Objects with Method

class Student:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(self.name)

obj1 = Student("Asha")
obj2 = Student("Riya")

obj1.show()
obj2.show()

# Output:
# Asha
# Riya


# 6. Object Updating Value

class Student:
    def __init__(self, name):
        self.name = name

obj = Student("Sneha")

obj.name = "Priya"

print(obj.name)

# Output:
# Priya



# 7. Class with Multiple Attributes

class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

obj = Student("Sneha", 21, "MSc IT")

print(obj.name)
print(obj.age)
print(obj.course)

# Output:
# Sneha
# 21
# MSc IT

