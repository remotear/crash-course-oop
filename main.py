from geometri.bangunruang import BangunRuang
from geometri.persegipanjang import PersegiPanjang
from geometri.segitiga import Segitiga

print('Mengunakan OOP')

s1 = Segitiga(4, 2)
print(s1.info())
print(s1.hitung_luas())

p1 = PersegiPanjang(10, 3)
print(p1.info())
print(p1.hitung_luas())

print('\nMembuat object dari kelas BangunRuang')
b1 = BangunRuang()
print(b1.info())
print(b1.hitung_luas())

# Polymorphism: kemampuan object untuk merespon berbeda, terhadap pemanggilan method yang sama
daftar_bangun_ruang = []
daftar_bangun_ruang.append(p1)
daftar_bangun_ruang.append(s1)

print('\nPolymorphism')
for bangun_ruang in daftar_bangun_ruang:
    print(bangun_ruang.info())

