import random                    #import dahil etme, kütüphaneyi ekle anlamına gelmektedir.

for i in range(5):               #range(5): 5 kez tekrar et.i değişkendir. İstenilen harf kullanılabilir.
    r = random.randint(0, 10)    #random.randint(0, 10): 0 ila 10 arasında random bir sayı verir.
    print(r)
                                 #if'i for'un içine yazdığımız için 5 kez tekrar etmektedir.
                                 #For'un içinde devam etmesi için 4 boşluk(1 tab) bırakarak yazılmalıdır.
    if r == 5:                            
        print("Sayi 5'e eşit")            #Eğer for ile aynı hizada olursa sadece 1 kez tekrar edecektir.
    elif r < 5:
        print("Sayi 5'ten küçük")
    else:
        print("Sayi 5'ten büyük") 

#Her 4 boşluk(1 TAB) önceki fonksiyonun içinde çalıştırılması için kullanılmaktadır.
