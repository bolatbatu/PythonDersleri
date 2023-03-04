#Dosya Okuma
with open("dosya_adi.txt","r")  as dosya:    #eğer dosya_adi.txt bu açılan uygulama ile aynı doyada ise sadece ismi kullanılabilir.
    icerik = dosya.read()                    #dosya işlemi yapılır.
    print(icerik)
#Dosya Yazma
with open("dosya_adi.txt","w")  as dosya:    #eğer dosya_adi.txt bu açılan uygulama ile aynı doyada ise sadece ismi kullanılabilir.
    icerik = dosya.write()
    print(icerik)