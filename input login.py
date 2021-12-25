# no 1 & 2
y=0
while (y<=3):
    username = (input())
    password = (input())
    berhasil1 = "luwakwhitecofee"
    berhasil2 = "kopinikmatnggabikinkembung"
    if username == berhasil1 and password == berhasil1:
        print("selamat anda berhasil login")
    else :
        print("login gagal")
        y += 1
        print()


# no 4
for i in range (1,50,3):
    print(i,end=" ")


a=50
while (a>0):
    for i in range (1,a,3):
        print(i,end=" ")
    a-=1
    print()

a=50
while (a>0):
    b=1
    while (b<a):
        print(b,end=" ")
        b+=3
    print()
    a-=1

# no 3
for b in range (0,a,29):
    a= 0
    for a in range (4,14,4):
    a=a+1
    print(a,end=" ")
print(b,end=" ")




    