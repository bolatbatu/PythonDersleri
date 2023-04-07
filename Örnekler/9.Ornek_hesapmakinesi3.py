#! HESAP MAKİNESİ

def hesap_makinesi(islem):
    if islem=="+":
        def topla():
            try:    
                sayilar=[]
                while True:
                    sayi=int(input("Sayı giriniz"))
                    sayilar.append(sayi)
                    if sayi==0:
                        sayilar.pop(-1)
                        break
                y=0
                for i in sayilar:
                    y+=i
            except:
                print("Hatalı İşlem")    
            print(y)
        topla()

    if islem=="-":
        def cikar():
            sayilar=[]
            while True:
                sayi=int(input("Sayı Giriniz"))
                sayilar.append(sayi)
                if sayi==0:
                    sayilar.pop(-1)
                    break
            a=sorted(sayilar)
            s=a[-1]
            for i in sayilar[1:]:
                s-=i
            print(s)

        cikar()
    if islem=="*":
        def carp():
            try:
                sayilar=[]
                while True:
                    sayi=int(input("Sayı Giriniz"))
                    sayilar.append(sayi)
                    if sayi==0:
                        sayilar.pop(-1)
                        break
                y=1
                for i in sayilar:
                    y*=i
            except:
                print("Hatalı işlem")
            print(y)
        carp()
    if islem=="/":
        def bol():
            try:
                sayi1=int(input("Sayı giriniz"))
                sayi2=int(input("Sayı giriniz"))
            except:
                print("Hatalı işlem")          
            print(sayi1/sayi2)
        bol()
while True:
    islem=input("işlem: ")
    hesap_makinesi(islem)
    if islem=="0":
        break