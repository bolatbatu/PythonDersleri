#break/continue Döngüleri.

for i in range(1,10):
    if i == 5 :                    #5'e gelince duracak. 5 dahil edilmeyecek.
        break
    print(i)                       #sonuc = 1,2,3,4

for i in range(1,10):
    print(i)                       #sonuc = 1,2,3,4,5
    if i == 5:                     #print if'ten önce yazılırsa 5 dahil edilir.
        break

for i in range(1,10):
    if i == 5 :                    #5'e gelince duracak. 5 dahil edilmeyecek ve devam edecek.
        continue
    print(i)                       #sonuc = 1,2,3,4,6,7,8,9