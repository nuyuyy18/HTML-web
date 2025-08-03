matrix1 = [
    [1, 2],
    [3, 4]
]
matrix2 = [
    [5, 6],
    [7, 8]
]

if len(matrix1[0]) != len(matrix2):
    print("Error: Dimensi Matrix tidak sesuai untuk perkalian")

hasil = [[0 for row in range(len(matrix2[0]))] for col in range(len(matrix1))]
# biar tidak error, maka sebelum input diberi angka 0

for baris in range(len(matrix1)):
    for kolom in range(len(matrix2[0])):
        for k in range(len(matrix2)):
            hasil[baris][kolom] += matrix1[baris][k] * matrix2[k][kolom]

print("Hasil Perkalian Matrix: ")
print(hasil)

# matrix1 = [
#     [1, 2]
#     [3, 4]
# ]
# matrix = [
#     [5, 6]
#     [7, 8]
# ]
