class Araba:                                                                                  #Araba için istenilen bilgiler için class oluşturduk.
    def __init__(self, marka, model, renk, plaka):
        self.marka = marka
        self.model = model
        self.renk = renk
        self.plaka = plaka
        
class ParkYeri:                                                                                #Park yeri hakkında bilgisi.
    def __init__(self, ID):
        self.ID = ID
        self.doluluk_durumu = False
        self.araba = None

    def araba_park_et(self, araba):
        self.doluluk_durumu = True
        self.araba = araba

    def araba_cikar(self):
        self.doluluk_durumu = False
        self.araba = None
        
class Otopark:
    def __init__(self, kapasite):
        self.kapasite = kapasite
        self.park_yerleri = [ParkYeri(ID) for ID in range(kapasite)]

    def bos_park_yeri_sayisi(self):
        return sum(not park_yeri.doluluk_durumu for park_yeri in self.park_yerleri)

    def bos_park_yeri_bul(self):
        for park_yeri in self.park_yerleri:
            if not park_yeri.doluluk_durumu:
                return park_yeri
        return None

    def araba_park_et(self, araba):
        if self.bos_park_yeri_sayisi() == 0:
            return "Otopark dolu"
        bos_park_yeri = self.bos_park_yeri_bul()
        bos_park_yeri.araba_park_et(araba)
        return f"{araba.plaka} plakalı araç otoparka park edildi."

    def araba_cikar(self, plaka):
        for park_yeri in self.park_yerleri:
            if park_yeri.doluluk_durumu and park_yeri.araba.plaka == plaka:
                park_yeri.araba_cikar()
                return f"{plaka} plakalı araç otoparktan çıkarıldı."
        return "Araba bulunamadı."

def araba_ekle(otopark):
    marka = input("Araba markası: ")
    model = input("Araba modeli: ")
    renk = input("Araba rengi: ")
    plaka = input("Araba plakası: ")
    araba = Araba(marka, model, renk, plaka)
    sonuc = otopark.araba_park_et(araba)
    print(sonuc)

def araba_cikar(otopark):
    plaka = input("Araba plakası: ")
    sonuc = otopark.araba_cikar(plaka)
    print(sonuc)

def bos_park_yerleri(otopark):
    bos_park_yeri_sayisi = otopark.bos_park_yeri_sayisi()
    print(f"{bos_park_yeri_sayisi} boş park yeri var.")



while True:
    print("""
        1 - Araba Ekle
        2 - Araba Çıkar
        3 - Boş Park Yeri Sayısı
        4 - Çıkış
        """)
    secim = input("Seçiminiz: ")
    if secim == "1":
        araba_ekle(otopark)
    elif secim == "2":
        araba_cikar(otopark)
    elif secim == "3":
        bos_park_yerleri(otopark)
    elif secim == "4":
        break
    else:
        print("Geçersiz seçim.")