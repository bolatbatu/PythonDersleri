sayi = int(input("Sayi Giriniz:")) 
toplam=0
for i in range(1,sayi):
    if(sayi%i == 0):                   #Sayıyı tam bölen sayıları i olarak ele alıyoruz ve topluyoruz.
        toplam +=i     
print ("Mükemmel Sayidir." if sayi == toplam else "Mükemmel Sayi Degildir")
#Sayı ve Toplam'ı birbirine eşit ise mükemmel sayıdır.