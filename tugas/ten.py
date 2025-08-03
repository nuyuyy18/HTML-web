x = input("masukkan sandi anda ")

if len (x) >= 8:
    print("Strong")
if len (x) in range(5, 8):
    print("Moderate")
else:
    print("Weak")

