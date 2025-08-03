input = input("Masukkan Input: ")

list = [int(n) for n in 
input.split(",")]

nilai_max = max(list)
nilai_min = min(list)

print(f"Nilai Maksimum Adalah: {nilai_max}")
print(f"Nilai Minimum Adalah: {nilai_min}")
