x = float(input("masukkan input skor siswa "))
if x in range(90, 101):
    print("A")
elif x in range(80, 89):
    print("B")
elif x in range(70, 79):
    print("C")
elif x in range(60, 69):
    print("D")
else:
    print("F")