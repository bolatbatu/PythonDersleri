t = 1
f = 0

if t and t == True:
    print("True")
if t and f != bool(True):
    print("False")
if f and t != bool(False):
    print("False")
if f and f == bool(False):
    print("False")

#And kondisyonunda en başa 0 gelince(f=0 olduğu için) işleme almıyor, sadece ilk 2 kondisyon çalışıyor.

print("--------------------------------------")

if t or t ==True:
    print("True")
if t or f != False:
    print("True")
if f or t != False:
    print("True")
if f or f == False:
    print("False")
