masa = {1:"",2:""}
menü = {"doner":10, "lahmacun":5, "kola":3}
while True:
    girdi_m = input("""         
    1*Sipariş al           
    2*Hesap al
    3*Çıkış
    """)                             #3 tırnak işarti içerisinde daha düzgün görünmesi için kullanılmaktadır.
    if girdi_m =="1":  
        girdi = input("masa numarası seçiniz:")
        print(girdi)
        siparis = input("siparis giriniz:")
        if siparis == "doner":
                masa[int(girdi)] += "doner"
        elif siparis == "lahmacun":
                masa[int(girdi)] += "lahmacun"
        elif siparis == "kola":
                masa[int(girdi)] += "kola"
        print(masa)
    elif girdi_m == "2":
        ücret = 0
        girdi = input("masa seçimi yapınız:")
        print(girdi)
        yiyecekler = masa [int(girdi)].strip()            #.strip boşlukları silmek için kullanmaktadır.
        yiyecekler = yiyecekler.split()                   #Karakter dizisinin nereden bölüneceğini seçer.
        print(len(yiyecekler))                            #Liste içerisindeki ürünleri sayar.( 2 adet ürün içerir)
        print("masa adisyonu", yiyecekler)
        print("--------------------------------")
        for yiyecek in yiyecekler:                       #her bir işlem için çalışır. 3 işlem için 3 kez çalışır.
            ücret = ücret + menü[yiyecek]                #Dictionary içerisindeki rakamları seçmek için kullanılır.
            print("Fiyat : ", ücret)                     #Topla ücreti göstermek için kullanılır.
    elif girdi_m == "3":
        break