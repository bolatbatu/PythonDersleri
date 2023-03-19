class Car:                                                        #Arabanın iskeletini oluşturduk.         
   def __init__(self, name,colour, type, engine, hp):             #Arabanın gösterilmesini istediğimiz özellikleri listeledik.
     self.name = name     
     self.colour = colour                      
     self.type = type
     self.engine = engine
     self.hp = hp
     self.tire_count = 4

car_1 = Car("Ferrari","Red", "Sport Car", "Gasoline" ,4000 )      #İlk arabanın özellikleri.        
car_2 = Car("Subaru","Blue", "4x4", "Gasoline", 1600)             #İkinci arabanın özellikleri.

print("-----------------------------")                            #car_! ile yukarıda girdiğimiz class değerlerini eşleştirerek gözlemleyebildiğimiz komutlar.
print("Araba'nın adı:",car_1.name)
print("Arabanın Rengi:",car_1.colour)
print("Arabanın tipi:",car_1.type)
print("Motor:",car_1.engine)
print("Beygir:",car_1.hp)
print("Silindir:",car_1.tire_count)
print("-----------------------------")
print("Araba'nın adı:",car_2.name)
print("Arabanın Rengi:",car_2.colour)
print("Arabanın tipi:",car_2.type)
print("Motor:",car_2.engine)
print("Beygir:",car_2.hp)
print("Silindir:",car_2.tire_count)