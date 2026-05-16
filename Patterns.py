#1. Square Star Pattern

rows = 5

for i in range(rows):
    for j in range(rows):
        print("*", end=" ")
    print()

# Output:
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *

#2. Right Triangle Star Pattern

rows = 5

for i in range(1, rows + 1):
    print("* " * i)

# Output:
# *
# * *
# * * *
# * * * *
# * * * * *


#3. Inverted Right Triangle

rows = 5

for i in range(rows, 0, -1):
    print("* " * i)

# Output:
# * * * * *
# * * * *
# * * *
# * *
# *


# 4. Pyramid Pattern

rows = 5

for i in range(rows):
    print(" " * (rows - i - 1), end="")
    print("* " * (i + 1))

# Output:
#     *
#    * *
#   * * *
#  * * * *
# * * * * *

#5. Inverted Pyramid Pattern

rows = 5

for i in range(rows, 0, -1):
    print(" " * (rows - i), end="")
    print("* " * i)

# Output:
# * * * * *
#  * * * *
#   * * *
#    * *
#     *

# 6. Right Pascal Triangle Pattern

rows = 5

for i in range(1, rows + 1):
    print("* " * i)

for i in range(rows - 1, 0, -1):
    print("* " * i)

# Output:
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *


# 7. Number Triangle Pattern

rows = 5

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# Output:
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5


# 8. Same Number Pattern

rows = 5

for i in range(1, rows + 1):
    print((str(i) + " ") * i)

# Output:
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5



# 9. Alphabet Triangle Pattern

rows = 5

for i in range(rows):
    for j in range(i + 1):
        print(chr(65 + j), end=" ")
    print()

# Output:
# A
# A B
# A B C
# A B C D
# A B C D E



# 10. Floyd’s Triangle Pattern

rows = 5
num = 1

for i in range(1, rows + 1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()

# Output:
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15
