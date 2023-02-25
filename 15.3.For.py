liste1 = [1,2,3]
liste2 = ["a","b","c"]

for eleman in zip(liste1,liste2):               #2 listeyi birleştirmek için kullanılır.
    print(eleman)

isimler = ["Ahmet","Mehmet","Ali"]
yaslar = [25,30,35]

sozluk = dict(zip(isimler,yaslar))
print(sozluk)