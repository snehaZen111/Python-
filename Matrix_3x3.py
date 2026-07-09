# Input a 3x3 matrix
matrix = []

print("Enter the elements of the 3x3 matrix:")

for i in range(3):
    row = []
    for j in range(3):
        element = int(input(f"Enter element [{i}][{j}]: "))
        row.append(element)
    matrix.append(row)

# Display the matrix
print("\nThe 3x3 Matrix is:")
for row in matrix:
    print(row)
