class kedi:
    name = "kedi"                        #Eğer name sabit ise classın altına yazılır. Yeni oluşturulacak objelerde bu isim kullanılacak.
    #tricks = []                         #Eğer dışarıya tricks listesi açarsak yazılan her yetenek her kedi için kullanılıyor olacaktır.
    def __init__(self,yaş):
        self.yaş = yaş                   #Değişken olarak yaşını ayarladık. Kedilerin isimleri kedidir ama yaşları farklı olabilir.
        self.tricks = []                 #Her kedi için yetenek listesi oluşturulur.
    def add_trick(self,trick):
        self.tricks.append(trick)
k = kedi(2)                              
h = kedi(5)
k.add_trick("yuvarlan")
h.add_trick("Uyu")

k.name
print(h.name)                            #Kedinin yaşı değiştirilebilir fakat ismi kedi olarak kalır.
k.yaş
print(h.yaş)
print(h.tricks)