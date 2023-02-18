#-------------------------------------Kondisyonlar-----------------------------------------------
# 
#if      #eğer anlamına gelmektedir. Kondisyon doğru ise çalışmaktadır.
#elif    #if kondisyonu çalışmıyorsa bu kondisyon çalışır.
#else    #if ve elif çalışmazsa else kondisyonu devreye girmektedir.

a = 5
b = 8


if a > b:
    print("if çaliştir.")
elif a < b:
    print("elif çalişir.")
else:
    print("else çalişir.")

#bu kondisyonda b>a olduğundan dolayı elif çalışmaktadır.
