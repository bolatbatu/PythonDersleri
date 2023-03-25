class kedigiller:
    def __init__(self,isim,boyut):
        self.isim = isim
        self.boyut = boyut
        self.renk = []                         #Kediye özgü rengi liste olarak kurduk.
    def sesliiletişim(self,ses):
        self.ses = ses
class kedi(kedigiller):                        #Inheritance(Miras alma). Kedigilleri kedi class'a aktardık.
    def renk(self,renk):
        self.renk.append(renk)
            
kedi = kedi("pamuk","3 inc")                   #kedi class'ından çektik. class kedi
kedi.renk = ("sarı")                           #Renk def'inden çektik. self.renk
kedi.ses = "Miyavlama"                         #Ses def'inden çektik. self.ses

print(kedi.isim,kedi.boyut,kedi.renk,kedi.ses)


