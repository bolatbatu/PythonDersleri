#Encapsulation----Kapsüllenme ile dışarıdan tamamen erişimi engellemeye yarar. Erişebilmek için fonksiyon kullanılmaktadır.
class calisan:
    def __init__(self,maas,ad):
        self.__maas = maas           #Encapsulation yapılarak maas'a erişim engellendi.
        self.__ad = ad
    def maas_göster(self):           #Fonksiyon ile erişim engeli olan __maas'a erişebildik.
        print(f"{self.__maas}TL maaş ")

    def maas_degistir(self,yeni_maas):
        self.__maas = yeni_maas

c_1=calisan(1000,"Batuhan")
c_2=calisan(1000,"Alperen")

c_1.maas_göster()                    #Fonksiyonu kullanarak maas'a erişebiliyoruz.
c_2.maas_degistir(3000)
c_2.maas_göster()                    #Değişen maaşı göstermek için tekrardan komut kullandık çünkü self.__maas, yeni_maas'a dönüştü. Tekrardan print yapılınca yeni maaş gösterilecektir.

#c_1.maas                            #Hata verir çalışmaz çünkü erişim engelli vardır.