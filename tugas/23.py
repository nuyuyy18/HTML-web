matrix1 = [[1, 2],[3, 4]]
matrix2 = [[5, 6],[7, 8]]

if len(matrix1) !=len(matrix2) or len(matrix1[0]) !=len(matrix2[0]):
    print("Matrix Harus Memiliki Ukuran yang sama")
else:
    hasil = []
    for i in range(len(matrix1)):
        baris_hasil = []
        for j in range(len(matrix1[0])):
            baris_hasil.append(matrix1[i][j] + matrix2[i][j])
        hasil.append(baris_hasil)

    print("Hasil Penjumlahan Matrix")
    print(hasil)

# ma = [
# [1, 2],
# [3, 4]
# ]
# mb = [
# [5, 6],
# [7, 8]
# ]
# 
# ma = [
# [1, 2],
# [3, 4]
# ]

# a = [1, 2]
# b = [3, 4]

# c = [a, b]

# print(ma)
# print(c) outputnya sama

# mx = [
#     [ma[0][0] + mb[0][0], ma[0][0] + mb[0][0]],
#     [ma[0][0] + mb[0][0], ma[0][0] + mb[0][0]]
# ]

# print("mx: ", mx)
# 