n = int(input("Masukkan Bilangan Faktor Positif: "))
i = 1
for i in range(1, n+1):
    if n % i == 0:
        print(n, "Adalah Faktor Dari ", i)