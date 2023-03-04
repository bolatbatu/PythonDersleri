#import os                                    #veri dosyası oluşturulduktan sonra bu kod silinir.
#os.mkdir("veriler")                          #veri dosyası oluşturulduktan sonra bu kod silinir.

for sayi in range(1,100,1): 
    veri_adi="veri_"+str(sayi)+".txt"    
    with open("veriler/"+veri_adi,"w")as file:
        file.write(veri_adi) 
