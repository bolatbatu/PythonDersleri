class banka:
    def __init__(self,ad,bakiye):
        self.__ad = ad
        self.__bakiye = bakiye

    def bakiye_goster(self):
        print(f"İsin : {self.__ad}\nMevcut Bakiyeniz:{self.__bakiye}TL")

    def bakiye_ekle(self,bakiye):
        self.__bakiye = self.__bakiye + (bakiye - (bakiye/10))
        print("Yeni Bakiye eklendi.")

kullanıcı=banka("Mehmet",15000)
kullanıcı.bakiye_goster()
kullanıcı.bakiye_ekle(35000)
kullanıcı.bakiye_goster()

