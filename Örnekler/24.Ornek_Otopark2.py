class Arac:
    def __init__(self, marka, model, renk, plaka,giris_saati):
        self.marka = marka
        self.model = model
        self.renk = renk
        self.plaka = plaka
        self.giris_saati = giris_saati

    def ucret_hesapla(self, cikis_saati):
        giris_saat_dakika = int(self.giris_saati[:2]) * 60 + int(self.giris_saati[3:])  #[:1]Sürenin ilk iki sayısını alır (11.33 ise 11'i ele alır.)
        cikis_saat_dakika = int(cikis_saati[:2]) * 60 + int(cikis_saati[3:])            #[3:]Sürenin 4.ifadesi ile başlar(11.43 ise 43 ü eler alır.)
        sure_dakika = cikis_saat_dakika - giris_saat_dakika
        ucret = sure_dakika // 60 * 20                                                  #Tam bölümüyle 20'yi çarptığımızda saat başı ücretini hesaplarız.
        if sure_dakika % 60 > 0:                                                        #Eğer tam bölümü ile kalan varsa 15TL ek ücret alınacaktır.
            ucret += 15
        return ucret
        
    def __str__(self):
        return f"{self.marka} {self.model} ({self.renk}) - {self.plaka}"

class ParkYeri:
    def __init__(self):
        self.doluluk = False
        self.arac = None

    def park_et(self, arac):
        self.doluluk = True
        self.arac = arac

    def arac_cikar(self):
        self.doluluk = False
        arac = self.arac
        self.arac = None
        return arac
    def __str__(self):
        
        return "Dolu" if self.doluluk else "Boş"

class Otopark:
    def __init__(self, kapasite):
        self.kapasite = kapasite
        self.park_yerleri = [ParkYeri() for i in range(kapasite)]

    def bos_park_yeri_sayisi(self):
        return sum([1 for park_yeri in self.park_yerleri if not park_yeri.doluluk])

    def bos_park_yerleri(self):
        return [i for i, park_yeri in enumerate(self.park_yerleri) if not park_yeri.doluluk]

    def dolu_park_yeri_sayisi(self):
        return sum([1 for park_yeri in self.park_yerleri if park_yeri.doluluk])

    def park_yeri_sayisi(self):
        return len(self.park_yerleri)

    def arac_bul(self, plaka):
        for park_yeri in self.park_yerleri:
            if park_yeri.doluluk and park_yeri.arac.plaka == plaka:
                return park_yeri
        return None

    def arac_park_et(self, arac):
        if self.bos_park_yeri_sayisi() == 0:
            return False
        bos_park_yerleri = self.bos_park_yerleri()
        park_yeri_index = bos_park_yerleri[0]
        self.park_yerleri[park_yeri_index].park_et(arac)
        return True

    def arac_cikar(self, plaka):
        park_yeri = self.arac_bul(plaka)
        if park_yeri is None:
            return False
        arac = park_yeri.arac_cikar()
        return arac


class Vale:
    def __init__(self, otopark):
        self.otopark = otopark

    def arac_teslim_et(self, arac):
        if self.otopark.arac_park_et(arac):
            print(f"{arac} park edildi.")
        else:
           
            print("Otoparkta boş yer yok!")

    def arac_iade_et(self, plaka):
        arac = self.otopark.arac_cikar(plaka)
        if arac:
            print(f"{arac} çıkarıldı.")
        else:
            print(f"{plaka} plakalı araç bulunamadı.")

otopark = Otopark(10)
valet = Vale(otopark)

while True:

    secim = int(input("""
    1*Otopark'a arac ekle
    2*Otoparktan arac cikart
    3*iptal

    Seciminizi Giriniz:"""))
    if secim == 1:
        print("Araç ekleniyor.")
        aracismi = input("Araç ismi:")
        modeli = input("Modeli:")
        renk = input("Rengi:")
        plakası = input("Plaka")
        giris = input("Giris saatiniz:")
        arac = Arac(aracismi,modeli,renk,plakası,giris)
        valet.arac_teslim_et(arac)
    elif secim == 2:
        print("Araç teslim için plaka giriniz.")
        cikis = input("Cikis saatiniz:")
        teslim = input("Plaka giriniz:")
        ucret = arac.ucret_hesapla(cikis)
        valet.arac_iade_et(teslim)
        print(f"Ücret: {ucret:.2f} TL")
    elif secim == 3:
        break
    else:
        print("Geçersiz işlem.")