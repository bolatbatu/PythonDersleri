#------------------integer---------------------------
int_1 = 5                                               #tam sayı için kullanılır.                                       
#------------------String----------------------------
str_1 = "ahmet"                                         #Metinler için kullanılır.
str_2 = "5"                                         
#------------------Bool------------------------------
bool_1 = True                                           #Doğru ve yanlış değerleri saklamak için kullanılır.
#------------------Float-----------------------------
float_1 =1.5555                                         #Tam sayı olmayan ifadeler için kullanılır.


#sayı ile başlanmaz. (_)ile başlanabilir. Örnek olarak; _bool_1 , _str_1 gibi.

#----------------------------------------------------------------------------------------------------#

print(int_1)
print(str_1)
print(bool_1)
print(float_1)

print(type(int_1))                                      #Fonksiyonun hangi tür/sınıfta olduğunu gösteriyor.
print(type(float_1))

print(int_1-float_1)
print(type(int_1-float_1))                              #Çıkan sonucun hangi class'ta olduğunu gösterir.
print(int_1-int(str_2))                                 #str'yi int olarak çevirmeden işlem gerçekleşmez.
print(type(int_1-int(str_2)))

#str_1'i int çeviremezsin çünkü ahmet bir sayı değildir.

degisken = 1
Degisken = 2

print(degisken)                  #Büyük ve küçük harfe duyarlıdır. Degisken olarak yazılırsa cevap 2 olur.