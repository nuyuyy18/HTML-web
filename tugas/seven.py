
year = float(input("masukkan input tahun "))
    
if year % 4 == 0:
    print("Tahun Kabisat")
    if year % 100 == 0:
        print("Bukan Tahun Kabisat")
        if year % 400 == 0:
            print("Tahun Kabisat")           
