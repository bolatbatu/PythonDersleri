n = int(input("Sayı giriniz:"))

def factorial(n):                        #Faktoriyel için bir fonksiyon  oluşturduk.
    if n==1:                             #Eğer faktoriyel 1 ise sonuç 1'dir.
        return 1
    else:
        return n*factorial(n-1)          #Faktoriyel kendisi ve kendisinden önceki rakamların çarpımı olduğundan oluşturduğumuz komut.

print(factorial(n))                      #n kadar oluşturulan faktoriyel komut dizimi.