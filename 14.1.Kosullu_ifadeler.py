sayi = int(input("Sayi giriniz."))
sayi2 = int(input("Sayi giriniz."))

#TEK SEVİYELİ İF KOŞULLU ÖRNEĞİ---------------------------------------------

if sayi == 5 :                                #Sadece koşulu kontrol eder.
    print("tek koşul doğru")
#ÇİFT SEVİYELİ İF KOŞULU ÖPRNEĞİ----------------------------------------------

if sayi == 6:
    print("Çift koşu doğru")                  #Koşulu kontrol eder. Koşul yanlışsa else komutu çalışır.
else:
    print("Çift koşul yanlış")
#BİRLEŞİK SEVİYELİ İF KOŞULU ÖRNEĞİ----------------------------------------------

if sayi == 7:
    print("birleşik koşul if doğru")
elif sayi == 8:                               #Koşulu kontrol eder. Koşul yanlışsa elif komutu çalışır. Elif'te yanlışsa else komutu çalışır.
    print("Birleşik koşul elif doğru")
else:
    print("birleşik koşul yanlış")
#SON SEVİYE İF KOŞULU ÖRNEĞİ-------------------------------------------------------   

if sayi == 1 :                                #iç içe if koşulu kullanılabilir.
    if sayi2 == 2:                            #ilk koşul sağlanırsa içindeki koşul'a bakılır.
        print("Son seviye if içinde if koşulu doğru")
    else:
        print("Son seviye if içinde if komutu yanlış")
elif sayi == 3 :
    sonuc = "Doğru" if sayi2 == 4 else "Yanlış"
    print(sonuc)
else:
    print("Son seviye koşul komutu yanlış")

#sonuc = "Doğru" if koşul else "Yanlış"        #TERNARY >> Tek satırda if/else komutu kullanılabilir.