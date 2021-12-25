# # no 0
# for a in range(0,100):
#     a= a+1
#     print('saya tidak akan mencontek lagi',a)
# # no1

# a = 10
# while (a>0):
#     # loopx
#     # b = 0
#     # while (b<a):
#     #     print("*",end="")
#     #     b +=1
#     print("aku")
#     a = a

# # no2 
# for a in range (1,11):
#     for b in range (1,a):
#         print(b,end="")
#     print()


# # # no3
# for b in range (10,0,-1):
#     for c in range (1,b):
#         print(c,end="")
#     print()

# # no4
# loop y
y=10
while(y>0):
    x=0
    while (x>y):
        print(x,end="")
        x+=1
    print()
    y=y-1

# masukkan = "ya"
# count = 2
# while (masukkan == "ya"):
#     count= count-1
#     masukkan = input("masukkan ")
#     print("perulangan ke",count)

#     if masukkan == "no" :
#         print("mandek")
#         break

# while True:
#     tinggi = int(input("masukkan tinggi"))
#     if tinggi == 160:
#         print("tebakan benar")
#         # break
#     else:
#         print("tebakan salah")

# z = "Ensyse"

# x = 0
# print(z[0:-1])

# # for i in z :
# #     x = x + 1
# #     print(z[0:x])

# for i in z :
#     x = x - 1
#     print(z[0:x])

for i in range(0,5):
    for j in range(i,3):
        print("*",end=" ")
    print()

y = 0
while (y<4):
    for i in range(4):
        print('+',end='')
        y=y+1
    print()