class kitap:
    """
    örnektir."""

    def __init__(self,ad,yazar,sayfa):
        self.ad = ad
        self.yazar = yazar
        self.sayfa = sayfa

    def __str__(self):

        return super().__str__()+ "\nAdı:{}\nyazarı:{}\nsayfa sayısı:{}".format(self.ad,self.yazar,self.sayfa)
    
    def topla():
        pass                                            #Hatayı es geçiyor.

#   def __del__(self):                                  #Veri silmeye yarar.
#       super().__del__()
#       print("Kitap silindi.")

    def __dict__(self):                                 #Dictionary olarak oluşturur.
        return {"ad":self.ad,"yazar":self.yazar,"sayfa_sayisi":self.sayfa}

k1 = kitap("Doğa üstü", "Batuhan Bolat", 352)
k2 = kitap("Aden","Batuhan Bolat",250)

print(k1)
print(k2)                            #<__main__.kitap object at 0x0000011DD165FA10> adresini verir.

del k2                               #k2'yi siler.
                 

#print(k1.__class__)                 #Hangi classtan üretildiği gösterilir.
#print(k1.__delattr__(k1.ad))        #Kitabın adını siler.
#print(k1.__dict__)                  #Dictionary'e aktarır.
#print(k1__doc__)                    #Yukarıda verilen """ içindeki yorumu gösterir.(sonuç=örnek)
#print(k1.__ge__)                    #>><<  ifadelerin nasıl davranacağını gösterir.
#print(k1__getattribute__)           #Geri dönün string'in ayarlanamsını sağlar.
#print(k1.__hash__())                #Şifrelenmiş algoritmayı gösterir.
#print(k1__init_subclass__)          #üst classta olmayan ama alt clasta olmasını istediğimiz şeyler için kullanılır.
#print(k1_.__module__)               