class Araba:
    def __init__(self, marka, model, renk, plaka):
        self.marka = marka
        self.model = model
        self.renk = renk
        self.plaka = plaka

class ParkYeri:
    def __init__(self, numara):
        self.numara = numara
        self.araba = None

    def bos_mu(self):
        return self.araba is None

    def araba_cek(self):
        araba = self.araba
        self.araba = None
        return araba

class Otopark:
    def __init__(self, kapasite):
        self.kapasite = kapasite
        self.park_yerleri = []
        for i in range(kapasite):
            self.park_yerleri.append(ParkYeri(i+1))

    def bos_park_yeri_sayisi(self):
        sayac = 0
        for park_yeri in self.park_yerleri:
            if park_yeri.bos_mu():
                sayac += 1
        return sayac

    def bos_park_yeri_bul(self):
        for park_yeri in self.park_yerleri:
            if park_yeri.bos_mu():
                return park_yeri
        return None

    def araba_girisi(self, araba):
        park_yeri = self.bos_park_yeri_bul()
        if park_yeri:
            park_yeri.araba = araba
            print(f"{araba.marka} {araba.model} {araba.renk} renkli araç otoparka girdi. Park yeri: {park_yeri.numara}")
            return True
        else:
            print("Otopark dolu!")
            return False

    def araba_cikisi(self, plaka):
        for park_yeri in self.park_yerleri:
            if park_yeri.araba and park_yeri.araba.plaka == plaka:
                araba = park_yeri.araba_cek()
                print(f"{araba.marka} {araba.model} {araba.renk} renkli araç otoparktan çıktı. Park yeri: {park_yeri.numara}")
                return True
        print(f"{plaka} plakalı araç otoparkta bulunamadı!")
        return False

class Terminal:
    def __init__(self, otopark):
        self.otopark = otopark

    def menu_goster(self):
        print("""
        1- Araç Girişi
        2- Araç Çıkışı
        3- Boş Park Yeri Sayısı
        4- Çıkış
        """)

    def calistir(self):
        print("Otopark Yönetim Sistemine Hoş Geldiniz!")
        while True:
            self.menu_goster()
            secim = input("Lütfen bir işlem seçin: ")
            try:
                secim = int(secim)
            except ValueError:
                continue

            if secim == 1:
                marka = input("Marka: ")
                model = input("Model: ")
                renk = input("Renk: ")
                plaka = input("Plaka: ")
                araba = Araba(marka, model, renk, plaka)
                self.otopark.araba_gir
            elif secim == 2:
                plaka = input("Plaka: ")
                self.otopark.araba_cikisi(plaka)

            elif secim == 3:
                bos_park_yeri_sayisi = self.otopark.bos_park_yeri_sayisi()
                print(f"Otoparkta {bos_park_yeri_sayisi} adet boş park yeri bulunmaktadır.")

            elif secim == 4:
                print("Otopark Yönetim Sisteminden çıkış yapılıyor...")
                break
            
otopark = Otopark(50)
terminal = Terminal(otopark)
terminal.calistir()