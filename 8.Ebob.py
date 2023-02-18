import math
while True:
    print("1* Ebob Uygulamasi")
    print("2* Çikis")
    secim = int(input("Seçim: "))
    if secim == 2:                                  #Eğer 2'yi seçersek komut kapaınır.
        break
    if secim == 1:                                  #Eğer 1'i seçersek ebob komutu çalışır.
        sayi_1 = int(input("sayi 1 : "))
        sayi_2 = int(input("sayi 2 : "))
        ebob = math.gcd(sayi_1,sayi_2)              #EBOB için komut dizimi.
        print("{} ve {} sayilarinin ebobu {} ".format(sayi_1,sayi_2,ebob)) 
        #bu kod komutu ile verdiğimiz sayıları ve ebobunu rahatça gözlemleyebiliriz.
        #verdiğimiz sayılar .format fonsiyonu ile sırasıyla {} içlerine yazılacaktır.