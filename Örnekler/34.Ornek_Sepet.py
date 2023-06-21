shpcrt = {     "laptop": 12500.00,
               "mouse": 750.50,
               "headphone": 1250.50,
               "klavye": 2450.00,
               "mousepad": 250.00,
               "144hz": 3500.00,
               "240hz": 9500.00,
               "kulaklık": 350.00,
               "hoparlör": 905.00,
               "rgbklavye": 3250.00,
               }         
order = []
total = 0

print("--------- SHOPING CART ---------")
for key, value in shpcrt.items():                                
    print(f"{key:10}: {value:.2f} TL")                         
print("------------------------")
while True:
    liste = input("\nİstediğiniz cihazı seçiniz (sipariş bittiyse 'd'ye basınız. Silmek istediğiniz ürün için 'sil' yazınız.): \n").lower()     
    if liste == "d":                                                                         
        break
    elif liste == "sil":                                                                     
        order.remove(input("silinecek siparişinizi seçiniz:"))
    elif shpcrt.get(liste):                                                                     
        order.append(liste)
    else:
        print("\nÖZÜR DİLERİZ, İSTEDİĞİNİZ ÜRÜN MAĞAZADA YOKTUR! LÜTFEN YUKARIDAKİ CİHAZ LİSTESİNDEN SEÇİNİZ")

print("------ Siparişiniz ------")
for liste in order:
    total += shpcrt.get(liste)                                            
    print("Siparişleriniz>>>", liste, end ="\n\n")
    
print(f"Toplam ücretiniz: {total:.2f} TL\n\n")                        
