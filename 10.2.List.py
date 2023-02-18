liste1 = []                                               #oluşturulacak listeyi boş bıraktık.
while True:         
    print(liste1)
    print("1* Listeye ekle")
    print("2* Listeden çikart")
    print("3* Listele")
    print("4* Çikis")
    secim = int(input("Seçim: "))                         #Seçeceğimiz rakama göre döngü oluşturuldu.
    if secim == 4:
        break
    if secim == 1:
        liste1.append(input("eklenecek malzeme:"))        #Listeye nesne ekleme.
    if secim == 2:
        liste1.remove(input("silinecek malzeme:"))        #Listeyeden nesne çıkartma.
    if secim == 3:
        print(liste1)
        break
