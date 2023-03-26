class Hayvanlar:
    def __init__(self, isim, yas, tur):
        self.isim = isim
        self.yas = yas
        self.tur = tur
    
    def konus(self):
        print("Hayvanlar konuşamaz")

    def bilgilendirme(self):
        print("isim:",self.isim)
        print("yas:",self.yas)
        print("tur:",self.tur)

class kuslar(Hayvanlar):                                  #Yukarıda verilen bilgilere erişim sağlar bir nevi miras alır.
    def __init__(self, isim, yas, tur, yumurta):
        super().__init__(isim, yas, tur)                  #Bir üst sınıfın nitelik ve metotları üzerinde değişiklik yaparken, mevcut özellikleri de muhafaza edebilmemizi sağlar.
        self.yumurta = yumurta

    def bilgilendirme(self):
        super().bilgilendirme()
        print("yumurta : ",self.yumurta)
    
    def özelligi(self):                                   #Yukarıda verilen bilgiyi miras alır ve kullanacağımız kısma göre değişim sağlar.
        print("kuşlar uçuyor.")

    def konus(self):
        print("Tavuklar öter.")
class tilki(Hayvanlar):
    def __init__(self, isim, yas, tur, yumurtayer):
        super().__init__(isim, yas, tur)                  #Super().__init__ , yukarıda verilen __init__'e erişim sağlamaya yarar.        
        self.yumurtayer = yumurtayer

    def bilgilendirme(self):
        super().bilgilendirme()
        print("yumurta:",self.yumurtayer)

    def özelligi(self):
        print("tilki avlanıyor.")
    
    def konus(self):
        print("Tilki cıyaklar")

tilki1 = tilki("Tilki",1,"tilki","yer")
kuslar1 = kuslar("tavuk",2,"kus","yapar")
print("--------------------")
tilki1.bilgilendirme()
tilki1.özelligi()
tilki1.konus()
print("--------------------")
kuslar1.bilgilendirme()
kuslar1.özelligi()
kuslar1.konus()