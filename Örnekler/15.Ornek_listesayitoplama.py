liste1=[]

def toplama():
    toplam = sum(liste1)
    return toplam

while True:
    secim=int(input("1*ekle, 2*topla, 3*çıkış"))
    if secim == 1:
        liste1.append(int(input("sayı ekle")))
    if secim == 2:
        toplama()
        print ('Dizi toplamı : ',toplama())
    else:
        print("çıkış yapıldı.")
