def sayi_arttir(x):
    return x+1
def sayi_azalt(x):
    return x-1
def ikiye_böl(x):
    return x/2

def işlem(sayi,fonk):
    if fonk == ikiye_böl:
        if sayi == 0:
            print("Sıfıra bölünemez!")
            return

    sonuc=fonk(sayi)
    print(sonuc)

işlem(3.75, ikiye_böl)