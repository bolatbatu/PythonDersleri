import os                                           
#os.mkdir("veriler")                                 #veri dosyası oluşturulduktan sonra bu kod silinir.

#Yukarıda kodlar dosya oluşturduktan sonra silinmezse hata verir.
#Hata vermemesi için ya kod silinir ya da alttaki kod yazılır.

"""try:
    os.mkdir("veriler")                              #Dosya oluşturmak için kullanılan komut.
except FileExistsError:                              #Hata kaynaklanınca kapanmasını engellemek için kullanıldı.
    print("Halen varolan bir dosya oluşturulamaz:")"""


#99 adet .txt dosyası oluşturma.

for sayi in range(1,100,1): 
    veri_adi="veri_"+str(sayi)+".txt"    
    with open("veriler/"+veri_adi,"w")as file:       #veriler dosyasına veri.txt oluşturmak için kullandık. ve bu verilerin içine veri adlarını yazdık.
        file.write(veri_adi) 
