list = ["muz","ayva","karpuz"]
list.append("salatalık")            #Listeye nesne(salatalık) ekler. Listenin sonuna
list.append("kavun")
list[2:4] = "frambuaz", "kayısı"    #Listedeki 2 ve 4. nesneyi değiştirir.
list.remove("muz")                  #Listedeki nesneyi siler.(Muzu listeden çıkartır.)
list.sort()                         #Listeyi büyükten küçüğe sıralar.
#list.reverse()                     #Listeyi sondan başa şeklinde yazar.
print(list)