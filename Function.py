# 1. Simple Function

def greet():
    print("Hello World")

greet()

# Output:
# Hello World


---

# 2. Function with Parameters

def add(a, b):
    print(a + b)

add(5, 3)

# Output:
# 8


---

# 3. Function with Return Value

def multiply(a, b):
    return a * b

result = multiply(4, 5)
print(result)

# Output:
# 20


---

# 4. Function with Default Parameter

def student(name="Guest"):
    print("Hello", name)

student()
student("Sneha")

# Output:
# Hello Guest
# Hello Sneha


---

# 5. Function with Multiple Arguments

def total(*numbers):
    print(sum(numbers))

total(10, 20, 30)

# Output:
# 60


---

# 6. Keyword Arguments

def info(name, age):
    print(name, age)

info(age=21, name="Sneha")

# Output:
# Sneha 21


---

# 7. Lambda Function

square = lambda x: x * x

print(square(6))

# Output:
# 36


---

# 8. Function Calling Another Function

def add(a, b):
    return a + b

def show():
    result = add(2, 3)
    print(result)

show()

# Output:
# 5


---

# 9. Function with List

def show_list(items):
    for i in items:
        print(i)

fruits = ["Apple", "Banana", "Mango"]

show_list(fruits)

# Output:
# Apple
# Banana
# Mango


---

# 10. Recursion Function

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))

# Output:
# 120

