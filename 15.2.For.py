#Liste elemanlarına index numaralarını ekleme.

liste = ["a","b","c","d"]
for i, eleman in enumerate(liste):                #listedeki elemanların yanına sayı ekler.
    print(i,eleman)                               #sonuc = 0 a   1 b    2 c   3 d

print("---------------------------------------------------------------------")

#index numarasının başlama değeri belirleme

liste = ["a","b","c","d"]
for i, eleman in enumerate(liste, start=1):       #listedeki elemanların yanına sayı ekler.
    print(i,eleman)                               #sonuc = 1 a   2 b    3 c   4 d

#Bu ifadeler bir şeyi sayı ile listeleme gibi ifadelerde kullanılır.
