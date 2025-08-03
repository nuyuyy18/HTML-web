n = int(input("Masukkan Input: "))

def fibonacci_rekursif(n):
    if n <= 1:
        return n
    else:
        return fibonacci_rekursif(n-1) + fibonacci_rekursif(n-2)

hasil = fibonacci_rekursif(n)
print(f"Bilangan Fibnacci ke-{n} Adalah: {hasil}")




