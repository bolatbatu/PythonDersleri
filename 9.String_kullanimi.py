#myscr = input("Değer giriniz.")        #İçerisine argüman yazmak için kullanılır.
myscr = "html.www.site.com"
myscr = myscr.replace("html","****")    #html yazısını **** ile değiştirilmesini sağlayan komut.
myscr = myscr.upper()                   #myscr'nin içinde bulunan metini büyüten bir komut.#
print(myscr[::-1])                      #Yazıyı tersten göstermesini sağlayan komut dizimi.(moc.etis...)
#print(myscr[0])                        #ilk harf verir.(h)
#print(myscr[0:7])                      #ilk 7 harfi verir.(html.ww)
#print(myscr[0:7:2])                    #iki adımda bir okur.(hm.w)
#print(myscr[::-2])                     #Yazıyı ikişer atlayarak tersten göstermesini sağlayan komut dizimi.