#100 adet veri.txt dosyası oluşturma ve bu verilerin 80 adetini set içinde traine 20 adetini ise set içinde test'e atmak adlı uygulama.

import os
import shutil                                               #Kopyalamak için kullanılan kütüphane.
try:                                                        #Kod 2.defa çalıştırıldığında aynı dosya olduğundan dolayı hata verecektir. Bu sebeple try-expect komutu kullanarak hata sonrası programın kapanmasını engelledik.
    os.mkdir("veri")
    print("veri dizini oluşturuldu")
except FileExistsError:
    print("veri dizini mevcut")

for i in range(1,101):                                      #100 adet veri oluşturma.
    with open("veri/veri_{}.txt".format(i), "w") as f:
        f.write("veri_{}".format(i))                        #verilerin içine yazı yazma.
print("veri dizini içerisine 100 adet dosya oluşturuldu")
try:
    os.mkdir(os.path.expanduser("~")+"/veri_seti")          #veri_seti dosyası oluşturma.
    print("veri_seti dizini oluşturuldu")
except FileExistsError:
    print("veri_seti dizini mevcut")

try:
    os.mkdir(os.path.expanduser("~")+"/veri_seti/train")    #veri_seti dosyası içinde train dosyası oluşturma.
    print("train dizini oluşturuldu")
except FileExistsError:
    print("train dizini mevcut")
try:
    os.mkdir(os.path.expanduser("~")+"/veri_seti/test")     #veri_seti dosyası içinde test dosyası oluşturma.
    print("test dizini oluşturuldu")
except FileExistsError:
    print("test dizini mevcut")

# veri dizini içindeki dosyaları test ve train dizinlerine 80-20 oranında kopyalama işlemi 
for i in range(1,101):
    if i <= 80:
        shutil.copy("veri/veri_{}.txt".format(i), os.path.expanduser("~")+"/veri_seti/train")
    else:
        shutil.copy("veri/veri_{}.txt".format(i), os.path.expanduser("~")+"/veri_seti/test")

print("veri dizini içerisindeki dosyalar test ve train dizinlerine 80-20 oranında kopyalandı")


            


