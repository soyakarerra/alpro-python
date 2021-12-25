class siswa():
    __nilai= 0 #private
    jurusan = "teknik industri"
    jumlah_siswa = 0
    def __init__(self,input_nama,input_nim):
        self.nama=input_nama #public
        self.nim=input_nim #public
        siswa.jumlah_siswa += 1
pajri = siswa("pajri supajri",1202111111)
lili = siswa("lililululalallele",130219777)

pajri.jurusan= "teknik industri perkapalan"

print(pajri.jurusan)
print(lili.jurusan)
print(siswa.jurusan)
print(pajri.__dict__)
print(lili.__dict__)

print(siswa.jumlah_siswa)



hargaBeras=[14000,12500,13000,10000,11000,11000,9750]
def mean(hargaBeras):
    jumlah=0
    for s in hargaBeras:
        jumlah += s
        return jumlah/len(hargaBeras)

print("Mean Harga Beras\t:","Rp",mean(hargaBeras))



# def modus():
#     modus = max(set(data), key=data.count)
#     a = data.count(modus)
#     b = []
#     for i in data:
#         if a - 1 < data.count(i):
#             b.append(i)
#     c = b[::a]
#     modus1 = 'Modus data adalah '
#     modus2 = []
#     if len(c) == 1:
#         modus1 += str(c[0])
#     else:
#         for i in c:
#             modus2.append(str(i))
#         modus1 += ' & '.join(modus2)
    
#     print(modus)
#     return
