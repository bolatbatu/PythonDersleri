def toplama1():                               #Örnek fonksiyon örneği.
    s1=5
    s2=7
    global sonuc                              #python 2'den kalan bir özellik.
    sonuc = s1+s2

toplama1()
print(sonuc)                                  #sonuc = 12.

"""def faktoriyel(sayi):
    sonuc=1
    for i in range(1,sayi,1):
        i *=1
        return i"""

global_degisken = 10                           #global değişken olarak tanımalayabiliriz.
def fonksiyon():
    yerel_degisken = 5
    print("global_degisken:",global_degisken)  #global değişken aynı zamanda fonksiyon içinde tanımlanabilir.
    print("yerel_degisken:",yerel_degisken)    #yerel değişken sadece fonksiyon içinde tanımlanabilir.
    def fonksiyon2():
        yerel2_degisken = 3
        print("global_degisken:",global_degisken)  
        print("yerel_degisken:",yerel_degisken) #Fonksiyon içindeki başka bir fonksiyonda kullanılabilir.
        print("yerel2_degisken:",yerel2_degisken)  
    fonksiyon2()

fonksiyon()
print("global_degisken:",global_degisken)