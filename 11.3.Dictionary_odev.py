menu = {       "pizza": 39.00,
               "makarna": 45.50,
               "mısır": 6.00,
               "fries": 25.50,
               "cips": 12.00,
               "kola": 15.50,
               "soda": 13.00,
               "limonata": 14.25,
               "doner": 90.50,
               "iskender": 110.00,
               "beyti": 90.50,
               "salata": 10.00,
               "su": 5.00,}
table = {"masa1":1,"masa2":2,"masa3":3,"masa4":4,"masa5":5,"masa6":6,"masa7":7,"masa8":8,"masa9":9}         
order = []
table_n = []
total = 0

print("--------- MENU ---------")
for key, value in menu.items():                                #Düzenli bir menü oluşturmak için kullanılmaktadır.
    print(f"{key:10}: {value:.2f} TL")                         #key : dan öncekş boşluk sayısını belirtir. (value:.2f)ise rakam belirtir.
print("------------------------")
while True:
    number = input("Masa numaranızı giriniz.").lower()         #yazılan lower komutu yazdığımız tüm metni küçük yazmamızı sağlar. Böylece Büyük ve küçük yazabiliriz.
    if  table.get(number):                                     #.get komutu yukarıda verilen listeyi getirir. Fooda yazılan metin yularıdaki listede yoksa ilerlemektedir.                                                                                
        table_n.append(number)                                 #listeye ürün ekler.
        break
    else:                                                                                                                       
        print("\nGirdiğiniz masa numarası geçersizdir. Tekrar giriniz!\n")
while True:
    food = input("\nİstediğiniz yemeği seçiniz (sipariş bittiyse 'd'ye basınız. Silmek istediğiniz ürün için 'sil' yazınız.): \n").lower()     
    if food == "d":                                                                          #d basılırsa sipariş alınmış olacak.
        break
    elif food == "sil":                                                                      #sil yazılırsa istenilen sipariş silinir.                                              
        order.remove(input("silinecek siparişinizi seçiniz:"))
    elif menu.get(food):                                                                     #menu içerisinde bulanan metinleri order üzerinde listeleyecek.
        order.append(food)
    else:
        print("\nÖZÜR DİLERİZ, İSTEDİĞİNİZ ÜRÜN MENÜMÜZDE YOKTUR! LÜTFEN YUKARIDAKİ MENÜDEN SEÇİNİZ")

print("------ Siparişiniz ------")
for food in order:
    total += menu.get(food)                                            #menü içerisinde bulunanları toplar.
    print("Siparişleriniz>>>", food, end ="\n\n")
    
print("masa numaranız: {} \n\n".format(number))                        #\n sonraki yazı için alt satıra geçer.
print(f"Toplam ücretiniz: {total:.2f} TL\n\n")                         #Ürünün toplam fiyatı için kullanılmaktadır.(f"{total:.2f} TL ") komutu toplam fiyatı gösterir.
