# 1. Create and Write File

file = open("demo.txt", "w")
file.write("Hello Python File Handling")
file.close()

print("File Created and Data Written")

# Output:
# File Created and Data Written


---

# 2. Read File

file = open("demo.txt", "r")
content = file.read()
file.close()

print(content)

# Output:
# Hello Python File Handling


---

# 3. Append Data in File

file = open("demo.txt", "a")
file.write("\nThis is new line added")
file.close()

print("Data Appended")

# Output:
# Data Appended


---

# 4. Read File Line by Line

file = open("demo.txt", "r")

for line in file:
    print(line.strip())

file.close()

# Output:
# Hello Python File Handling
# This is new line added


---

# 5. Using with open() (Best Method)

with open("demo.txt", "r") as file:
    print(file.read())

# Output:
# Hello Python File Handling
# This is new line added


---

# 6. Read File into List

file = open("demo.txt", "r")
lines = file.readlines()
file.close()

print(lines)

# Output:
# ['Hello Python File Handling\n', 'This is new line added']


---

# 7. Check File Handling (Try Except)

try:
    file = open("abc.txt", "r")
    print(file.read())
    file.close()
except FileNotFoundError:
    print("File Not Found")

# Output:
# File Not Found


---

# 8. Write Numbers in File

file = open("numbers.txt", "w")

for i in range(1, 6):
    file.write(str(i) + "\n")

file.close()

print("Numbers Written")

# Output:
# Numbers Written


---

# 9. Read First Line Only

file = open("demo.txt", "r")
print(file.readline())
file.close()

# Output:
# Hello Python File Handling


---

# 10. File Delete Concept (import os)

import os

if os.path.exists("demo.txt"):
    os.remove("demo.txt")
    print("File Deleted")
else:
    print("File Not Found")

# Output:
# File Deleted
