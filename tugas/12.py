n = int(input("Masukkan Bilangan: "))
           
for i in range(n):
    if i == 0:
        continue

    if (n % i == 0):
        a = i
        b = n / i
        
        print(a, " x ", b, " = ", n)

# n = int(input("Masukkan Input: "))
# a,b = 0,1 
# for _ in range(n):
#   print(a, end="")
#   a,b = b, a+b
    

    

