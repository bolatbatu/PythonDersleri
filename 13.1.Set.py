my_set = {1,2,3,4,5}                    #Set süslü parantez ile kullınılır.
set2 = {5,6,7,8,9}
#my_set.add(6)                          #Set'in içine 6'yı eklemek için kullanılan komut.
#my_set.remove(2)                       #Set'in içinden 2 'yi çıkartmak için kullanılır.
#set3 = my_set.union(set2)              #İki seti birleştirir.(set1+set2)
set3 = my_set.intersection(set2)        #İki seti kesiştirir. Ortak nesneleri alır.

#my_set = set1.difference(set2)          #İki seti bölger.Ortak olmayan nesneleri alır.
#lenght = len(my_set)                    #Setin uzunluğunu hesaplama.

print(set3)                  