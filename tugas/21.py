input = input("Masukkan Input Pisahkan dengan Koma: ")

list = [int(n) for n in 
input.split(",")]

average = sum(list) / len(list)
if average < 61:
    print("Tidak Lulus")
else:
    print("Lulus")

print(f"Rata-rata: {average}")


# Input dalam bentuk String
# Mengubah Input String menjadi List Angka
# list membuat data bisa diakses, dihitung, dibandingkan
# split = memisahkan string menjadi beberapa bagian
# loop for = memproses isi list satu persatu
# Menghitung Rata-Rata
# f-string(formatted string literals); string ("Rata-rata: {average}") tidak bisa digabung dengan float{average}
# itulah kenapa printnya harus diubah ke string dulu
# u/ menyisipkan nilai variabel langsung ke dalam string dg efisien