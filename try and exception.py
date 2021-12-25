# try:
#     n=int(input())
#     for a in range (1,n):
#         for b in range(a,str(a)*a)
#         print(b,end="  ")
# except ValueError :
#     print("Maaf, Inputan hanya menerima angka")

# try:
#     n=int(input())
#     for a in range (1,n):
#         print(str(a)*a,end="  ")
# except ValueError :
#     print("Maaf, Inputan hanya menerima angka")

print("ini adalah program pembagian")
while True:
    try :
        pembilang=int(input("masukkan pembilang:"))
        penyebut=int(input("masukkan penyebut:"))
        hasil=pembilang/penyebut
        break
    except ValueError:
        print("yang anda masukkan bukan angka cuy") 
    except ZeroDivisionError:
        print("jangan masukin nol pembagian pake nol gabisa yaa:))")

print("program telah beraakhir dan yang anda masukkan benar",hasil)
