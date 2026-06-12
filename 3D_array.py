# 3D Array Program

array_3d = [
    [
        [1, 2, 3],
        [4, 5, 6]
    ],
    [
        [7, 8, 9],
        [10, 11, 12]
    ]
]

print("3D Array Elements:")

for i in range(len(array_3d)):
    for j in range(len(array_3d[i])):
        for k in range(len(array_3d[i][j])):
            print(array_3d[i][j][k], end=" ")
        print()
    print()

# Output:
# 3D Array Elements:
# 1 2 3
# 4 5 6
#
# 7 8 9
# 10 11 12
