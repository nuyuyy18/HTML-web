x = int(input("Masukkan Input Angka: "))
n = int(input("Masukkan Input Pangkat: "))

def pangkat_rekursif(x, n):
    if n == 0:
        return 1
    elif n < 0:
        return 1 / pangkat_rekursif(x, -n) 
    else: 
        return x * pangkat_rekursif(x, n - 1)
    
hasil = pangkat_rekursif(x, n)
print(f"Hasil: ", hasil)

# aturan Eksponen, Jika suatu bilangan dibagi dengan dirinya sendiri, hasilnya adalah satu. Konsep ini diterapkan pada eksponen 0
    