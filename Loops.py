# 1. for Loop

for i in range(1, 6):
    print(i)

# Output:
# 1
# 2
# 3
# 4
# 5

# 2. for Loop with List

fruits = ["Apple", "Banana", "Mango"]

for item in fruits:
    print(item)

# Output:
# Apple
# Banana
# Mango

# 3. while Loop

i = 1

while i <= 5:
    print(i)
    i += 1

# Output:
# 1
# 2
# 3
# 4
# 5

# 4. Nested Loop

for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)

# Output:
# 1 1
# 1 2
# 1 3
# 2 1
# 2 2
# 2 3
# 3 1
# 3 2
# 3 3

# 5. Break Statement

for i in range(1, 6):
    if i == 4:
        break
    print(i)

# Output:
# 1
# 2
# 3

# 6. Continue Statement

for i in range(1, 6):
    if i == 3:
        continue
    print(i)

# Output:
# 1
# 2
# 4
# 5

# 7. Pass Statement

for i in range(5):
    pass

print("Loop completed")

# Output:
# Loop completed

# 8. range(stop)

for i in range(5):
    print(i)

# Output:
# 0
# 1
# 2
# 3
# 4

# 9. range(start, stop)

for i in range(1, 6):
    print(i)

# Output:
# 1
# 2
# 3
# 4
# 5

# 10. range(start, stop, step)

for i in range(1, 10, 2):
    print(i)

# Output:
# 1
# 3
# 5
# 7
# 9

# 11. Reverse Loop

for i in range(5, 0, -1):
    print(i)

# Output:
# 5
# 4
# 3
# 2
# 1
