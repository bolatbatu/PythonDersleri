kaleci = ("Ali", 27, "kaleci",1)             #Kaleci için değişmez bir liste oluşturduk(Tuple)

defans1 =("Hakan",25, "defans",2)
defans2 =("Hasan",22, "defans",3)            #defans için değişmez bir liste oluşturduk(Tuple)
defans3 =("Mehmet",18, "defans",4)
defans4 =("Murat",27, "defans",5)

orta_saha1 =("Bartu",20, "orta_saha",6)
orta_saha2 =("Yaman",21, "orta_saha",7)
orta_saha3 =("Yağız",23, "orta_saha",8)      #orta saha için değişmez bir liste oluşturduk(Tuple)
orta_saha4 =("Kemal",25, "orta_saha",9)

forvet1 =("Alp",23, "forvet",10)             #forvet için değişmez bir liste oluşturduk(Tuple)
forvet2 =("Batuhan",24,"forvet",11)

oyuncular = (kaleci, defans1,defans2,defans3,defans4,orta_saha1,orta_saha2,orta_saha3,orta_saha4,forvet1,forvet2)
                #Tüm oyuncularu bir tuple listesinde depoladık.
for oyuncu in oyuncular:                 #Oyuncuların hepsini listelemek için for kullandık. For her girilen bilgiyi tekrar etmek için kullanılır.
    print("Adı:", oyuncu[0])             #Her oyuncunun adını listede bulunan ilk nesneyi kullanacaktır.
    print("Yaşı:", oyuncu[1])            #Her oyuncu için yaşı listeden bulunan ikinci nesneyi kullanacaktır.
    print("Mevkii:", oyuncu[2])          #Her oyuncu için mevkii listeden bulunan üçüncünci nesneyi kullanacaktır.
    print("Forma Numarası:", oyuncu[3])  #Her oyuncu için forma numarasını listeden bulunan dördüncü nesneyi kullanacaktır.
    print("-" * 30)                      #30 adet - kullanmak için komut kullandık böylece her oyuncu sonrası karışmaması için - çekilecektir. 