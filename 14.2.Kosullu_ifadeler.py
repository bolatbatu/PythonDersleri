sayi_1 = int(input("\nilk sayi giriniz: "))                     
sayi_2 = int(input("ikinci sayiyi giriniz: "))
islem = input("Toplamak için (+): ")
print("\nİlk sayi+ : " ,sayi_1, "İkinci sayi : " ,sayi_2)

sonuc = sayi_1 + sayi_2 if islem =="+" else "Yanlış"
print("{} + {} = {} ".format(sayi_1,sayi_2,sonuc))            