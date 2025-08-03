# Dalam Python harus ada Indentasi/Penjorokan untuk menandai blok kode, misalnya pada perulangan atau percabangan
name = "Nuyuy" #str
age = 21 #int
height = 170.5 #float/angka dibelakang koma

print("haloo nama saya " + name)
print("Umur saya " + str(height)) #Integer tidak bisa digabung dengan string, makanya dibungkus dulu dg str baru integer 
angka1 = 100
angka2 = 50

print(angka1 - angka2 + angka2)
print(angka1 + angka2)
print(angka1 * angka2)
print(angka1 / angka2)
print(angka1 % angka2) #modulo -> sisa hasil bagi

sedangHujan = False 
sedangTerik = True 
# isRaining (apakah ...) boolean
# hasMoney (apakah punya ...) boolean
# print(sedangHujan) 3.
# print(sedangTerik) 4.

# conditional (IF boleh berdiri sendiri tanpa else, else ada hanyajika kondisi if tidak terpenuhi)
if sedangHujan:
    print("Jangan Lupa Bawa Payung")
else:
    print("Tidak Bawa Payung Karna Tidak Hujan")
    # print("Tidak Bawa Payung Karna Tidak Hujan") (Kode print boleh lebih dari satu yang penting masi satu baris)   
    print("Tidak Bawa Payung Karna Tidak Hujan")

uangSaya = 5000
hargaGame = 1000000

if uangSaya > hargaGame:
    print("Boleh Beli Game")
else:
    print("Tidak Boleh Beli Game")

uangSaya = 10000
hargaGame = 10000

if uangSaya >= hargaGame:
    print("Boleh Beli Game")
else:
    print("Tidak Boleh Beli Game")

# Negasi (!=) kebalikannya (==)
# Multi Condition ( and/or) (and) = jika ada lebih dari satu syarat baru bisa menambah and; (or) = cukup salah satu syarat terpenuhi udah bsa di print 

uangSaya = 10000
hargaGame = 10000
adaWaktu = False

if uangSaya >= hargaGame and adaWaktu:
    print("Boleh Bermain Game")
else:
    print("Tidak Boleh Bermain Game")

uangSaya = 10000
hargaGame = 10000
adaWaktu = False

if uangSaya >= hargaGame or adaWaktu:
    print("Boleh Bermain Game")
else:
    print("Tidak Boleh Bermain Game")

# beberapa if boleh dipasang dalam satu program
uangSaya = 20000
gamePS = 10000
gameXBOX = 15000
gasing = 2500

if uangSaya >= gamePS:
    print("Bisa Beli Game PS")
if uangSaya >= gameXBOX:
    print("Bisa Beli Game XBOX")
if uangSaya >= gasing:
    print("Bisa Beli Gasing")

# jika program if pertama sudah terpenuhi dia tidak akan mempedulikan program elif dibawahnya, jika belum terpenuhi maka dia akan ke if yang mencukupi
uangSaya = 5000
gamePS = 10000
gameXBOX = 15000
gasing = 2500

if uangSaya >= gamePS:
    print("Bisa Beli Game PS")
elif uangSaya >= gameXBOX:
    print("Bisa Beli Game XBOX")
elif uangSaya >= gasing:
    print("Bisa Beli Gasing")
else:
    print("Tidak Bisa Beli Apapun")

# Match Case = mirip if else, ini digunakan ketika kita mau membandingkan satu nilai dengan beberapa variable lain, digunakan agar sintaks lebih cantik
# cukup salah satu syarat terpenuhi untuk bisa masuk ke dalam case nya
day = 10
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
# _ = sbg simbol tidak ada syarat yang terpenuhi
    case _:
        print("No Day")
    
# List/Array (Dalam Dunia Pemrograman dihitungnya dari 0)
namaMurid = ["Agus", "Herman", "Bambang"]
print(namaMurid[1])
# cara akses (print(namaMurid[1]))
namaMurid = ["Agus", "Herman", "Bambang"]
namaMurid[0] = "Agusasi"
print(namaMurid)
#  cara ganti value dari variable data tipe string

# Panjang Listnya
namaMurid = ["Agus", "Herman", "Bambang"]
print(len(namaMurid))
# untuk ngeprint jumlah banyak murid
if len(namaMurid) > 10:
    print("Kelas Bisa Dimulai")
else:
    print("Kelas Tidak Bisa Dimulai")

# cara Menambahkan data baru 
namaMurid = ["Agus", "Herman", "Bambang"]
namaMurid.append("Kuncoro") 
# atau bisa menggunakan (.add)
namaMurid.remove("Agus")
# memasukkan data baru di akhir
print(namaMurid)

# List
    # Array = Pembungkusnya kurung persegi []
    # Tuple = Array tapi bebas, tidak bisa diubah, pembungkusnya Kurung biasa ()
    # Set = Pembungkusnya kurung Kurawal {}, tidak terindeks melalui {0 1 2 3}
    # Dictionary = contoh {firstname:"john", lastname:"doe"}
namaMurid = ["Agus", "Herman", "Bambang", "Kuncoro"]

if "Kuncoro" in namaMurid:
    print("Kuncoro hadir Bu!")

# Loop - for loop
namaMurid = ["Agus", "Herman", "Bambang", "Kuncoro"]
for i in namaMurid:
    print(i)

# While Loop = Syarat, jika mau mengulang sesuatu harus menggunakan syarat.
number = 1
while number < 5:
    print("Angka: " + str(number))
    number = number + 1
#  versi lebih singkatnya menggunakan for in range
for x in range(1, 5):
    print(x)

#  Function = Daftar blok kode yang dijalankan dan bisa dipanggil hanya dengan namanya saja.
#  Dengan satu fungsi yang sama bisa memanggil parameter yang berbeda, dan bisa memasukkan parameter yang berbeda, agar lebih dinamis
def greet(name, hobby):
    print("Namanya adalah " + name + " Hobinya Adalah " + hobby)

greet("Hilman", "Main Bola")
greet("Elsa", "Memasak")
greet("Anna", "Buat Boneka Salju")
# Function Return
def sum(a, b):
    return a + b
print(sum(10, 20))
print(sum(30, 40))

# Dictionary : Kita Membuat Objek dan objek ini mempunyai kata kunci atau sifat yang unik beserta beserta nilainya
# menggunakan kurung kurawal
pokemon = {
    "name": "Pikachu",
    "type": "Electric",
    "level": "25",
}
# jika mau lebih spesifik bisa dipanggil berdasarkan nilai yang diinginkan
print("Hi! " + pokemon["name"])
pokemon["level"] = 100
print(pokemon["level"])

# Menggabungkan kondisi if else di dalam sebuah fungsi
def cek_status_driver(jaket_dipakai, aplikasi_menyala):
    if jaket_dipakai and aplikasi_menyala:
        print("Driver Aktif, Siap Narik!🏍️")
    elif jaket_dipakai:
        print("Driver Stanby, Belum Buka Aplikasi📱")
    else:
        print("Driver Istirahat Sejenak💤")
    # contoh penggunaan : (ingat harus sesuai penggunaan tanda baca, baris dan spasinya, jika salah sedikit saja maka program tidak berjalan (TELITI!!!))
cek_status_driver(False, True)



# STDIN/STDOUT = Standard
# python range function u/ Fungsi range() mengembalikan serangkaian angka, dimulai dari 0 secara default, dan bertambah 1 (secara default), dan berhenti sebelum angka yang ditentukan.
# def is_leap(year):(disebut Function) ; is_leap (disebut nama function) ; year (disebut parameter)
# loop = program akan mengulang perintah yang sama 
# if = conndition
# for = loop
# while = loop
# def = fungsi
# Python
# /n artinya Enter
# Assignment Statement { user_name = variable }
                    #  {         = = operator }
                    #  {   "Alice" = Value    }

# Call Statement = { print("Name:", user_name) } "Name:", user_name (Argumen yang dipisahkan dengan koma, yang didalam kurung disebut Argumen)
                #  { print("Age:", user_age) }
                #  { print("Is Student:", is_student) }

# user_name = "Alice"  { String } 
# user_age = 30        { Integer }
# is_student = "True"  { Boolean }

# Statement : - Assignment(=)
            # - Function call(fn())
            # - Block(:) : if, for, while, def

# function:
# def is_leap(year):
#     leap = False
    
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else: 
#        return False 
    

# year = int(input()) (Jika tidak ada tidak bisa memasukkan input)
# print(is_leap(year)) (Jika tidak ada tidak bisa memnjalankan function)
# return karena perintahnya diminta return

# function fibonacci:
# def fib(n):
#     if (n == 1 or n == 2):
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
    
# print(fib(10))

# i - integer
# b - boolean
# u - unsigned integer
# f - float
# c - complex float
# m - timedelta
# M - datetime
# O - object
# S - string
# U - unicode string
# V - fixed chunk of memory for other type ( void )
# extend() = Jika kamu memiliki dua array dan ingin menggabungkannya menjadi satu

# gwee/cli(Command Line Interface)
# Windows Subsystem of linux
# Kernel dr bahasa inggris biji jagung kering buat popcorn (karena bagian kecil dan ngobrol langsung dengan software)
# Simulator
# Containerization/Virtual Machine
# Docker (Dipake buat Development)(Mac.Linux.Windows)
# VMware/epsx
# wget = apk u/ download jaman dulu
# rpg maker u/ bikin game seperti digimon jaman dlu
# thick besar lebih efektif
# LUA = Programm di Roblox
# Bentuk Sintaks di Game Roblox
# code editor yang lebih ramah memori yaitu vim









