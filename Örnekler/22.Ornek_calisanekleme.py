calisan_listesi = []

class Calisan:
    sirket = "Barben Co."
    def __init__(self, isim, soyisim, yas, maas, pozisyon):
        self.isim = isim
        self.soyisim = soyisim
        self.yas = yas
        self.maas = maas
        self.pozisyon = pozisyon

    def tam_isim(self):
        return f"{self.isim} {self.soyisim}"

class calisanlar(Calisan):

    def calisan_ekle():
        isim = input("İsim: ")
        soyisim = input("Soyisim: ")
        yas = int(input("Yaş: "))
        maas = float(input("Maaş: "))
        pozisyon = input("Pozisyon: ")
        yeni_calisan = Calisan(isim, soyisim, yas, maas, pozisyon)
        calisan_listesi.append(yeni_calisan)
        print("Yeni çalışan eklendi!")

    for i in range(1):
        calisan_ekle()

    for calisan in calisan_listesi:
        print(calisan.tam_isim(), "Yaş : ",calisan.yas, calisan.maas,"TL", calisan.pozisyon.upper())