
while True:
    sayi = int(input("sayi giriniz: ")) #Bu komutla istediğimiz değişken girilebilir. Örnek olarak ahmet ve 5 gibi.
    print(sayi)

    if sayi < 5:                           #yazılan sayı 5'ten büyükse yazdır.
        print("Sayiniz 5'ten küçüktür")
    elif sayi > 5:                         #yazılan sayı 5'ten küçükse yazdır.
        print("Sayiniz 5'ten büyüktür")
    else:                                  #yazılan sayı 5'e eşitse yazdır.
        print("Sayiniz 5'e eşittir")

    if sayi == 99:
        break                              #Programı sonlandırmak için bir komut ekledik.
print("Program Sonlandirildi.")
#Ctrl+C komutu while döngüsünü sonlandırır.