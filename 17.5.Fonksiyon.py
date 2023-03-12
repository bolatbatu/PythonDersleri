#----Faktoriyel Fonksiyonu----
def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5)) # 5*4*3*2*1 = 120 

#-----Fibonacci Fonksiyonu----
def Fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)
print(Fibonacci(7)) # 0 1 1 2 3 5 8 13