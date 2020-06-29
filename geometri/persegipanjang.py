class PersegiPanjang() :
    def __init__(self, p, l) :

        self.p = p
        self.l = l

    def info(self) :
        return F'Ini adalah object dari persegi panjang dengan panjang = {self.p} dan tinggi = {self.l}'

    def hitung_luas(self) :
        return self.p * self.l
