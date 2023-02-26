#Fonksiyon kullanılarak hesap makinesi oluşturma.

def toplama():                                               #Toplama fonksiyonu.
    sonuc=sayi1+sayi2
    print("\n{} + {} = {} ".format(sayi1,sayi2,sonuc))
    return sonuc
def cikartma():                                              #Çıkartma fonkisyonu.
    sonuc=sayi1-sayi2
    print("\n{} - {} = {} ".format(sayi1,sayi2,sonuc))
    return sonuc
def çarpma():                                                #Çarpma fonksiyonu.
    sonuc=sayi1*sayi2
    print("\n{} * {} = {} ".format(sayi1,sayi2,sonuc))
    return sonuc
def bölme():                                                 #Bölme fonksiyonu.
    sonuc=sayi1/sayi2
    print("\n{} / {} = {} ".format(sayi1,sayi2,sonuc))
    return sonuc

while True:

    #İşlemi seçiniz.
    print("\n1*Toplama(+)")
    print("2*Çıkartma(-)")
    print("3*Çarpma(/)")
    print("4*Bölme(*)")

    secim = input("\nYapmak istediğiniz islemi seciniz.(çikis için 'end' yaziniz.):")

    #İşlem yapılmasını istediğimiz 2 farklı değer giriniz.
    sayi1=int(input("İlk sayiyi giriniz:"))
    sayi2=int(input("İkinci Sayiyi giriniz:"))

    if secim == "+":
        toplama()
    elif secim == "-":
        cikartma()
    elif secim == "*":
        çarpma()
    elif secim == "/":
        bölme()
    elif secim =="end":
        print("Hesap makinesinden cikis yapildi.")
        break
    else:
        print("Yapmak istediğiniz işlem tanimsiz. Tekrardan seçiniz(+ - / *)")
