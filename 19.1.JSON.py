import json                                              #json bir modüldür. 

#19.3.data.json üzerindeki veriyi okuduk.

with open("19.4.data.json","r") as f:
    data=json.load(f)                                    #Data okumak için kullanılan komut.
print(type(data))                                        #json verisinin hangi type olduğunu gösteren komut.
print(data)                                              #Verinin içindekileri gösterir.
 