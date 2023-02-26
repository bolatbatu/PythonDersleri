x =input()
y= input()
def bolme (x,y):
    try:
        return x/y             #Bölme işlemi sırasında 0'a bölümünde hata ile karşılaşılacaktır.
    except ZeroDivisionError:
        print("Sifira bölmek mümkün değil")