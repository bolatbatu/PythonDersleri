class RegisterCourse:
    def __init__(self):
        self.name = "Batuhan"
        self.surname = "Bolat"
        self.__exam1 = 74                   #Dışarıdan erişilemez. Ya self.exam1 şeklinde yazılmalı ya da get yapılarak çağırılmalıdır.
        self.__exam2 = 80                   #Dışarıdan erişilemez. Ya self.exam2 şeklinde yazılmalı ya da get yapılarak çağırılmalıdır.
        self.__courses = []                 #Dışarıdan erişilemez. Ya self.courses şeklinde yazılmalı ya da get yapılarak çağırılmalıdır.

    def __add(self,course):
        self.courses.append(course)

    def getExam(self):                      #Dışarıdan erişilmesi için gerekli olan komut dizimidir.
        return self.__exam1

    def setExam(self,newVal):
        if newVal<0 or newVal>100 :
            raise ValueError("Sınav puanı 0'dan küçük ve 100'den büyük bir  değer olamaz ")    #Bu hata gelirse fırlatlamaya yarar. 

register = RegisterCourse()
register.setExam(-10)

#Biz burada sınav puanının  0’dan küçük ve 100’den büyük değer olma durumlarını kontrol etmiş olduk. 0 dan küçük olduğunda hatayı fırlatıyoruz.