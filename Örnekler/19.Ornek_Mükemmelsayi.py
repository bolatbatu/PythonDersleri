sayi = int(input("Sayi Giriniz:")) 
toplam=0
for i in range(1,sayi):
    if(sayi%i == 0):
        toplam +=i     
print ("Mükemmel Sayidir." if sayi == toplam else "Mükemmel Sayi Degildir")  