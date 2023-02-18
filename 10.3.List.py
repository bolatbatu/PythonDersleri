liste_1 = [1,2,3,4,5]
#liste_2 = liste_1             #liste_1 ve liste_2 aynı adreste olduğu için liste_1 değişince liste_2 de değişecektir. Adresleri değişsede aynı adreste olacaktr.
liste_2 = liste_1.copy()       #bu komut ile listeyi farklı adreste kopyaladı. Eğer liste 1 değişirse liste 2 aynı kalacaktır.
print(liste_1)
print(liste_2)
print(id(liste_1))             #id ile listenin bilgisayarda hangi adreste tutulduğu gösteriliyor.
print(id(liste_2))
