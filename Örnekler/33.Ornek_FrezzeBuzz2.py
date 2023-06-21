import random
liste=[]
for i in range(20):
    liste.append(random.randint(0, 100))
def Func():
        if i % 3 == 0 and i % 5 == 0:
            print(i,"-","frezzebuzz")
        elif i % 3 == 0:
            print(i,"-","frezze")
        elif i % 5 == 0:
            print(i,"-","buzz")
        else:
            print(i)
for i in liste:
    Func()
