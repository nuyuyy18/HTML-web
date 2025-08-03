n = int(input("masukkan angka Fibonacci: "))
def fib(n):

    if (n == 1 or n == 2):
        return 1
    else:
        return fib(n-1) + fib(n-2)
    
print(fib(n))

# n = int(input("masukkan angka: "))
# a,b = 0,1
# for _ in range(n):
#     print(a, end='')
#     a,b = b, a+b
# 
# kalo gamau pake i bisa pake underscore(_)
# 
# 