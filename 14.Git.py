def hesap_makinesi(islem):
    if islem=="+":
        def topla():
            try:    
                sayilar=[]
                while True:
                    sayi=int(input("Sayı giriniz"))
                    sayilar.append(sayi)
                    if sayi==0:
                        sayilar.pop(0)
                        break
                y=0
                for i in sayilar:
                    y+=i
            except ValueError:
                print("Hatalı Değer")
            except TypeError:
                print("Hatalı Değer")
            except KeyError:
                print("Hatalı Değer")
            except SyntaxError:
                print("Hatalı Değer")    
            print(y)
        topla()

    if islem=="-":
        def cikar():
            sayi1=int(input("Sayı giriniz"))
            sayi2=int(input("Sayı giriniz"))
            print(sayi1-sayi2)
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
            except ValueError:
                print("Hatalı Değer")
            except TypeError:
                print("Hatalı Değer")
            except KeyError:
                print("Hatalı Değer")
            except SyntaxError:
                print("Hatalı Değer")
            print(y)
        carp()
    if islem=="/":
        def bol():
            try:
                sayi1=int(input("Sayı giriniz"))
                sayi2=int(input("Sayı giriniz"))
            except ValueError:
                print("Hatalı Değer")
            except TypeError:
                print("Hatalı Değer")
            except KeyError:
                print("Hatalı Değer")
            except SyntaxError:
                print("Hatalı Değer")
            except ZeroDivisionError:
                print("Sıfıra Bölünemez")            
            print(sayi1/sayi2)
        bol()
while True:
    islem=input("işlem: ")
    hesap_makinesi(islem)
    if islem=="0":
        break