#Sifre olsturulmasi için ilk önce yapılış sıralamasını yapmamız lazım.
#1*random kütüphanesi kullanilacak.                                                 yapıldı.
#2*sifre uzunlugu secilecek                                                         yapıldı.
#3*sifre adeti secilecek                                                            yapıldı.
#4*rastgele sifreler gösterilecek.                                                  yapıldı.


import random
harfvesekil = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()>£#$½]}\|[{"           #oluşturulmasını istediğimiz harf ve işaretleri oluşturduk.
 
sifre_uzunlugu = int(input("Sifrenin karakter sayisi seciniz : "))
sifre_adeti = int(input("Sifrenin adet sayisini seciniz : "))
for x in range(0, sifre_adeti):                                                                               #Sifrenin kac adet olusturulacagini ayarladigimiz bir komut.
        sifre = ""
        for x in range(0, sifre_uzunlugu):
            sifre_karakter = random.choice(harfvesekil)                                                       #random.choice komutu verilen ifalerden rastgele bir şey secer.
            sifre      = sifre + sifre_karakter                                                               #Sifre, sifre_adeti kadar olmasini saglamak için sifre+sifre_karater yazilmalidir.
        print("Rastgele Şifreniz : " , sifre)