#Fibonacci Örneği;

adim = int(input("kacinci adima kadar? "))     #Girilecek ifadenin sayı olacağından dolayı girilecek sayıyı int olarak girdik.

#Fibonacci de ilk iki adım 0 ve 1 olarak başlamaktadır. Bu yüzden burası sabit.
n1, n2 = 0, 1
count = 0

if adim <= 0:                                  #Fibonacci pozitif sayılardan meydana gelmektedir.
   print("Lütfen pozitif sayi giriniz.")
elif adim == 1:                                #Fibonacci ilk adımı 1'dir. Else komut diziminde adım sayısına 1 verirsek sonuç 0 çıkacaktır. Bu nedenle bu elif komutu yazıldı.
   print("Fibonacci",adim,"adima kadar",":")
   print(n1)
else:
   print("Fibonacci:")                         #Fibonacci hesaplama.
   while count < adim:
       print(n1)
       ntoplam = n1 + n2                       #ntoplam ile sonraki sayinini toplami ntoplam olacak bir komut dizimi.
#Sayıların sürekli toplanmasını sağlayan komut dizimi.
       n1 = n2
       n2 = ntoplam
       count += 1                              #Her işlemden sonra count sayısı artacaktır ve ne zaman verdiğimiz adım sayısı ile eşit olursa o zaman duracaktır.