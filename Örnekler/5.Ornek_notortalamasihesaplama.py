#not ortalamasi hesaplama için ilk önce yapılış sıralamasını yapmamız lazım.
#1*notlar girilecek                                                            yapıldı.
#2*notlarin ortalamasi alınacak                                                yapıldı.
#3*notların geçip geçmediğini göreceğiz.                                       yapılmadı.

sayi = input("Virgül ile sayıları giriniz.: ")
 
print("Girdiğiniz Sayılar: {0}".format(sayi))
 
ortalama=sayi.split(",")                                                                #split(",") komutu ile virgülleri sileriz.
toplam = 0 
for n in ortalama:
   toplam = toplam + int(n)                                                             #sayilarin toplamini hesaplar.
 
print("GİRDİĞİNİZ SAYİLARİN NOT ORTALAMASI:{0:.2f} ".format(toplam / len(ortalama)))    #len(ortalama) ile kaç adet sayi olduğunu hesaplariz.
#format(toplam / len(ortalama)) ile sayilarin toplamini sayi adetine bölerek ortalamayi hesaplariz.
if ortalama != (toplam / len(ortalama)):
    print("Kaldınız.",sayi)
if ortalama > (toplam / len(ortalama)):
    print("Geçtiniz.",sayi)