import numpy as np
from math import sqrt
def to_int(c):
    return ord(c.upper()) - ord('A')
def to_str(x):
    return chr(int(x % 26) + ord('A'))

teks = list(map(to_int,input("Masukkan Pesan : ")))
kunci = list(map(to_int,input("Masukkan Kunci : ")))
n=int(sqrt(len(kunci)))
print(n)
#ENSKRIPSI
matriks_kunci = np.array(kunci).reshape(n,-1)
matriks_teks = np.array(teks).reshape(n,-1,order="F")
matriks_enkripsi = matriks_kunci.dot(matriks_teks)
enkripsi = " ".join(map(to_str,matriks_enkripsi.ravel(order="F")))
#DESKRIPSI
matriks_invers = np.linalg.inv(matriks_kunci).reshape(n,-1,order="F")
matriks_dekripsi = np.round(matriks_invers.dot(matriks_enkripsi))
deskripsi = " ".join(map(to_str,matriks_dekripsi.ravel(order="F")))

print(matriks_kunci)
print(matriks_teks)
print(matriks_enkripsi)
print("Hasil Enkripsi : ",enkripsi)
print(matriks_invers)
print(matriks_dekripsi)
print("Hasil Dekripsi : ",deskripsi)