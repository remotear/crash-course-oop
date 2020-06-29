from geometri.persegipanjang import PersegiPanjang
from geometri.segitiga import Segitiga

print('Mengunakan OOP')

s1 = Segitiga(4, 2)
print(s1.info())
print(s1.hitung_luas())

p1 = PersegiPanjang(10, 3)
print(p1.info())
print(p1.hitung_luas())
