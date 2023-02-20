set1 = set()
set2 = set()                                             
while True:         
    print("Set1:", set1, "||| Set2:",set2)
    print("1* Kümeye Eleman Ekle.")
    print("2* Kümeden Eleman Çıkart")
    print("3* Kümeleri Karşılaştırma")
    print("4* Çıkış")
    secim = int(input("Seçim: "))                         
    if secim == 1:
        while True:
            print("Seti Seçiniz.(set1=1/set2=2/iptal=3)")
            print("Set1:", set1, "||| Set2:",set2)
            secim2 = int(input("Seçim: "))
            if secim2 == 1:
                set1.add(input("Eklenecek eleman:")) 
            elif secim2 == 2:
                set2.add(input("Eklenecek eleman:"))
            elif secim2 == 3:
                break    
    if secim == 2:
        while True:
            print("Seti Seçiniz.(set1=1/set2=2/iptal=3)")
            print("Set1:", set1, "||| Set2:",set2)
            secim3 = int(input("Seçim: "))
            if secim3 == 1:
                set1.remove(input("Çıkartılacak eleman:")) 
            elif secim3 == 2:
                set2.remove(input("Çıkartılacak eleman:"))
            elif secim3 == 3:
                break    
    if secim == 3:
        print("Set1:", set1, "||| Set2:",set2)
        set3 = set1.difference(set2)
        print("Set1 ve Set2 > Ortak olmayan elemanları :" ,set3)
        set4 = set1.intersection(set2)
        print("Set1 ve Set2 > Ortak elemanları :" ,set4)
        set5 = set1.union(set2)
        print("Set1 ve Set2 > Birleşimi :" ,set5)
        if set1.issubset(set2) == True:
            print("Set1, Set2'nin alt elemanıdır.")           
        elif set1.issuperset(set2) == True:
            print("Set1, Set2'nin üst elemanıdır.")
        else:
             print("Set1, Set2'nin alt veya üst elemanı değildir.")
        break

    if secim == 4:
        break