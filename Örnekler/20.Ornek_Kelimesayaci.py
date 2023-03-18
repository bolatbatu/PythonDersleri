def word_count(str):                             #Kelimeler için oluşturulan fonksiyon.
    words = str.split()                          #Tüm kelimeleri split() ederek küçültüyoruz.
    counts = dict()                               
    for word in words:
        if word in counts:
            counts[word] += 1                    #Kelime 1'den fazla ise;
        else:
            counts[word] = 1                     #Kelime 1 ise;
    return counts
with open("Örnekler\Test.txt","r") as dosya:     #Kelimelerin sayılmasını istediğimiz doyayı açmak için bu komutu kullanıyoruz.
    icerik = dosya.read()                 
    a = word_count(icerik)                       #Yukarıda yazdığımı fonksiyonu istediğimz dosya ile çalıştırıyoruz.
    b = sorted(a,key=a.get,reverse=True)         #Value değerlerine göre sıralamamızı sağlan komut.
    for r in b:
        print(r, a[r])