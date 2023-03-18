def word_count(str):
    words = str.split()
    counts = dict()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts
with open("Örnekler\Test.txt","r") as dosya:    
    icerik = dosya.read()                 
    a = word_count(icerik)
    b=sorted(a,key=a.get,reverse=True)
    for r in b:
        print(r, a[r])