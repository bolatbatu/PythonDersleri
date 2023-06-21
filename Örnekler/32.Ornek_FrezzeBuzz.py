import random

def Func():
    for i in range(20):
        r = random.randint(0, 100)
        if r % 3 == 0 and r % 5 == 0:
            print(r,"-""frezzebuzz")
        elif r % 3 == 0:
            print(r,"-","frezze")
        elif r % 5 == 0:
            print(r,"-","buzz")
        else:
            print(r)

Func()
