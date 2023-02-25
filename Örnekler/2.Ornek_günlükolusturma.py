#günlük yapımı için ilk önce yapılış sıralamasını yapmamız lazım.
#1*boş bir sayfa oluşturulacak.                                                     yapıldı.
#2*günün tarihini girilecek.                                                        yapıldı.
#3*günlük içindeki notlar kaydedilecek ve tarihe göre görüntülenebilecek.           yapılamadı.
#4*günlük şifre ile girilebilecek.                                                  yapıldı.
#5*Günlük uygulamasi için logging kütüphanesi kullanılabilir.

günlük = []

while True:
    
    sifre = int(input("Sifrenizi giriniz: "))
    
    if sifre == 1602:
        while True:
            secim = int(input("1*Günlük yaz.\n2*Günlük oku."))
            if secim == 1:
                
                tarih = str(input("gün'ü giriniz."))
                     
                günlük.append(input("Gününüzün nasıl geçtiğini buraya yazabilirsiniz."))
            if secim == 2:
                secim_2 = str(input("Tarihi seçiniz."))
                if secim_2 == tarih:
                    print(günlük)
                    break
                else:
                    print("Girdiğiniz tarihte bir günlük bulunmamaktadır.")              
        break     
    else:
        print("Girdiğiniz şifre yanlıştır. Tekrar deneyiniz.")