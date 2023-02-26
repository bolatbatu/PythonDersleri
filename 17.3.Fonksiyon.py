def dis_fonksiyon():
    a =5
    def ic_fonksiyon():
        print(a*2)                      #dis_fonksiyon'daki a'yı iç_fonksiyonda kullanılabilmektedir.
    ic_fonksiyon()                      #ic_fonksiyon'u, dis_fonksiyon'da çalıştırması için kullanılır.

dis_fonksiyon()                         #Fonksiyon tanımını göstermek için kullanılır.