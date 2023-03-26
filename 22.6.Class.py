class Calisan:
    def __init__(self, ad, soyad, yas, maas):
        self.ad = ad
        self.soyad = soyad
        self.yas = yas
        self.maas = maas

    def __str__(self):
        return f"{self.ad} {self.soyad}, {self.yas} yaşında, {self.maas} TL maaş"   #verilen bilgileri kolayca çekmeye yarayan f-string komutu.

class CalisanListesi:
    def __init__(self):
        self.calisanlar = []

    def calisan_ekle(self, calisan):                     #CalisanListesine, calisandan miras alarak çalıştırdık.
        self.calisanlar.append(calisan)

    def calisanlari_listele(self):
        for calisan in self.calisanlar:
            print(calisan)

# CalisanListesi sınıfını kullanarak çalışan ekleyelim
calisanlarim = CalisanListesi()
calisanlarim.calisan_ekle(Calisan("Ali", "Yılmaz", 28, 5000))
calisanlarim.calisan_ekle(Calisan("Ayşe", "Kara", 35, 7500))
calisanlarim.calisan_ekle(Calisan("Mehmet", "Demir", 42, 10000))

calisanlarim.calisanlari_listele()              # CalisanListesi sınıfındaki calisanlari_listele() yöntemini kullanarak çalışanları listeledik.


#Bu şeklide de yazılabilir;

"""class Calisan:
    def __init__(self, ad, soyad, maas):
        self.ad = ad
        self.soyad = soyad
        self.maas = maas

    def tam_isim(self):
        return f"{self.ad} {self.soyad} {self.maas} TL"

calisan_listesi = []                                   # Boş bir çalışan listesi oluşturalım

yeni_calisan = Calisan("Ali", "Kara","15000")
calisan_listesi.append(yeni_calisan)                   # Yeni bir çalışani listeye ekleme.

diger_calisan = Calisan("Ayşe", "Beyaz","12250")
calisan_listesi.append(diger_calisan)

for calisan in calisan_listesi:                        # Tüm çalışanları yazdırma komutu.
    print(calisan.tam_isim())"""