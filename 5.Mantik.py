a = True
b = False

print(a and b) #ve   
print(a or b)  #veya
print(not a)   #a değil
print(not b)   #b değil

#                                         MANTIK TABLOSU
#---------------------------------------------------------------------------------------------------------

#   and(ve)             or(veya)              not(değil)

# a/b   sonuç          a/b   sonuç          a   a'   b   b'             True =1
# 1/1     1            1/1     1            1   0    1   0              False=0
# 1/0     0            1/0     1            0   1    0   1
# 0/1     0            0/1     1
# 0/0     0            0/0     0

#---------------------------------------------------------------------------------------------------------

c = 1
d = 0
#and----------------
print(bool(c and c))
print(bool(c and d))
print(bool(d and c))
print(bool(d and d))
#or------------------
print(bool(c or c))
print(bool(c or d))
print(bool(d or c))
print(bool(d or d))
#not-----------------
print(bool(not a))     #a değil
print(bool(not b))     #b değil
print(bool(not not a)) #a(değilinin değili)
print(bool(not not b)) #b(değilinin değili)
