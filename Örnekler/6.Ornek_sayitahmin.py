#Bilgisayarın belirlemiş olduğu sayiyi bulma. Deneme hakkiniz 10.

import random
i = 0                   

for i in range(1):               
    r = random.randint(0, 100)    
while i <= 10 :
    if i < 10:
        sayi = int(input("Sayi giriniz :"))
        if sayi == r:                            
            print("Sayiyi buldunuz. Bilgisayarın seçtiği sayi {}".format(sayi))
            i +=1
            break
        elif sayi < r:
            print(" Vermiş olduğunuz sayi küçüktür {} ".format(sayi))
            i+=1
        elif sayi > r:
            print("Vermiş olduğunuz sayi büyüktür {}" .format(sayi)) 
            i+=1
    elif i == 10:
        print("Hakkiniz tükendi. istenilen sayi {} ".format(r))
        i +=1
        break