def toplama(sayi1,sayi2):                  #Fonksiyon olarak tanımladık.
    sonuc=sayi1+sayi2                      #Tanımlanan fonksiyonu toplama olarak tanıttık.
    return sonuc                           #sonuc'u return ederek fonksiyonu tamamladık.
print(toplama(5,7))                        #print(toplama(5,7)) yaparak fonsiyonun içine sayılar vererek fonksiyonun cevabını görürüz.
print(toplama(9,9))

#def toplama():                            #Fonksiyonları bu yapı ile de kullanılabilir.
#    x=input()                             #Fonksiyona dışarıdan erişilemez.
#    y=input()
#    sonuc=x+y
#    return sonuc

def kare(sayi):                            #Karesini alma.
    sonuc = sayi**2
    return sonuc
print(kare(3))                             #Fonksiyonu çağırma.