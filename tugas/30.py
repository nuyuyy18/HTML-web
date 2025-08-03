def gcd_recursive(a, b):

    if b == 0:
        return a
    else:
        return gcd_recursive(b, a % b)
    
bilangan1 = int(input("Masukkan Input Pertama: "))
bilangan2 = int(input("Masukkan Input Kedua: "))
fpb = gcd_recursive(bilangan1, bilangan2)
print(f"FPB dari {bilangan1} dan {bilangan2} adalah {fpb}")

