filename = input("Dosya adını giriniz:")                        #İstenilen dosyanın adını giriniz.(Örnekler\Test.txt)
with open(filename,"r") as file:                                #Girilen dosya bu komut sayesinde açılacaktır.
    text = file.read().lower()
words=text.split()                                              #.split() ile girilen harflerin hepsi küçük olacak. Böylece büyük harf başlayan kelimeler yeni kelime sayılmayacak.
print("------------------\n Toplam kelime sayısı",len(words))
word_counts = {}

for word in words:
    if word in word_counts:
        word_counts[word]+=1                                    #Kelimeden bir adet daha varsa if koşulu içine girer.
    else:
        word_counts[word]=1                                     #Kelimeden bir adet varsa else koşuluna girer.
sorted_word_counts=sorted(word_counts,key=word_counts.get,reverse=True)
print("------------------\n Kelime adeti")
for word in sorted_word_counts:
    print(word,word_counts[word])