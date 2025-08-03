x = float(input("masukkan input umur "))
if x in range(1, 18):
    print("Dibawah Umur")
elif x in range(18, 65):
    print("Dewasa")
else:
    print("Lanjut Usia")
