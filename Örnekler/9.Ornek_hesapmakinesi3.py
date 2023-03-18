def Islem():
    try:
        print("Yapılacak işlemi seçin. \n1* Toplama \n2* Çıkartma \n3* Çarpma\n4* Bölme")
        secim = input("Hangi işlemi yapmak istersiniz? : ")
        sayi1 = int(input("1. Sayıyı girin : "))
        sayi2 = int(input("2. Sayıyı girin : "))
        if secim == '1':
            print(sayi1,"+",sayi2,"=", sayi1+sayi2) 
        elif secim == '2':
            print(sayi1,"-",sayi2,"=", sayi1-sayi2) 
        elif secim == '3':
            print(sayi1,"*",sayi2,"=", sayi1*sayi2) 
        elif secim == '4':
            print(sayi1,"/",sayi2,"=", sayi1/sayi2)
        else:
            print("Geçersiz bir işlem numarası girdiniz.")
    except ValueError():
        print("geçerli sayı giriniz.")
    except ZeroDivisionError():
        print("Sıfıra Bölünmez")
while True:
    Islem()