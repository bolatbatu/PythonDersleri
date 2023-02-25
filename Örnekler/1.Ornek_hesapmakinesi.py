#Hesap Makinesi yapımı için ilk önce yapılış sıralamasını yapmamız lazım.
#1*yapılacak hesap makinesi için ilk önce 2 adet sayı belirlenecek              yapıldı.
#2*verilen sayılar ile hangi işlemi yapacağımızı seçeceğiz.                     yapıldı.
#3*verilen sayıları ve sonucunu göstereceğiz.                                   yapıldı.

#----------------------------------------------------------------------------

#Girilecek sayıları seçiyoruz.

sayi_1 = int(input("\nilk sayi giriniz: "))                                  #\n ile daha temiz bir görünüm sağlamaktayız. Bir satır alta kayar.               
sayi_2 = int(input("ikinci sayiyi giriniz: "))

print("\nİlk sayi+ : " ,sayi_1, "İkinci sayi : " ,sayi_2)

#Yapılmasını istediğimiz işlemi seçiyoruz.

print("\n1*Toplama(+)")
print("2*Çıkartma(-)")
print("3*Çarpma(/)")
print("4*Bölme(*)")

#Seçtiğimiz işlemlerin while döngüsü ile tekrarlanmasını sağlıyoruz. "end" yazarak bitiriyoruz.

while True:
    islem = input()
    if islem == "+" :                                                          # "+"toplama
        sonuc = sayi_1 + sayi_2
        print("{} + {} = {} ".format(sayi_1,sayi_2,sonuc))            
    elif islem == "-" :                                                        # "-"çıkartma
        sonuc = sayi_1 - sayi_2
        print("{} - {} = {} ".format(sayi_1,sayi_2,sonuc)) 
    elif islem == "/" :                                                        # "/"bölme
        sonuc = sayi_1 / sayi_2
        print("{} / {} = {} ".format(sayi_1,sayi_2,sonuc)) 
    elif islem == "*" :                                                        # "*"çarpma
        sonuc = sayi_1 * sayi_2
        print("{} * {} = {} ".format(sayi_1,sayi_2,sonuc))                     #.format yapısı ile daha temiz bir görünüm sağlamaktayız.
    elif islem == "end":
        print("Hesap makinesinden çıkış yapıldı.")
        break
    

    