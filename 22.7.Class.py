#Abstraction---Tek class içinde __init__ (abstraction)soyutlama
class İşlemci:
    def __init__(self, isim, yıl,boyut,mhz):
        self.isim = isim
        self.yıl = yıl
        self.boyut = boyut
        self.mhz = mhz
    
    def bilgilendirme(self):
        print("Cihaz ismi:",self.isim)
        print("Cihaz Yılı:",self.yıl)
        print("Cihaz Boyutu:", self.boyut)
        print("Cihaz MHZ:",self.mhz)
#Inheritance---2 class içinde başka class'ı kullanma Inheritance(Miras alma)
class Nvidia(İşlemci):                                 
    def __init__(self, isim, yıl,boyut,mhz,RTX):
        super().__init__(isim, yıl,boyut,mhz)                  #Bir üst sınıfın nitelik ve metotları üzerinde değişiklik yaparken, mevcut özellikleri de muhafaza edebilmemizi sağlar.
        self.RTX = RTX

    def bilgilendirme(self):
        print("------NVIDIA------")
        super().bilgilendirme()
        print("İşlemci Teknolojisi : ",self.RTX)
        print("RTX teknolojisi kullanilabilir.")
        print("DLSS teknolojisi ile yüksek kalite ve performans sağlar.")
#Polymorphism---3 veya daha fazla class'ın farklı özelliklere sahip olması ise (Polymorphism)çok biçimlilik
class AMD(İşlemci):
    def __init__(self, isim, yıl,boyut,mhz,Ray_Tracing):
        super().__init__(isim, yıl,boyut,mhz)                  #Super().__init__ , yukarıda verilen __init__'e erişim sağlamaya yarar.        
        self.Ray_Tracing = Ray_Tracing

    def bilgilendirme(self):
        print("------AMD------")
        super().bilgilendirme()
        print("İşlemci Teknolojisi:",self.Ray_Tracing)
        print("Ray Tracing teknolojisi kullanabiliyor.")
        print("FSR teknolojisi ile yüksek performans sağlar")

Nvidia = Nvidia("4090",2022,"16gb","2230mhz","var")
AMD = AMD("7900XTX",2022,"16gb","2500mhz","var")

Nvidia.bilgilendirme()
AMD.bilgilendirme()
