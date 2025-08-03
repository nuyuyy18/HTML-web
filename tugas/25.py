matrix1 = [
    [1, 2],
    [3, 4]
]
matrix2 = [
    [1, 3],
    [2, 4]
]


for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
        matrix2[j][i] = matrix1[i][j]

print("Hasil Transpose Matrix: ")
print(matrix2)
