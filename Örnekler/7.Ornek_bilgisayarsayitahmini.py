#Bilgisayarin senin belirlemiş sayini bulma.
import random 

def pick_number():
    return random.randint(1,100)

def guess_number():
    number=pick_number()
    min_value= 1
    max_value = 100
    guess =(max_value+max_value)// 2
    steps =1

    while guess != number:
        if guess < number:
            min_value = guess +1
        else:
            max_value = guess -1
        guess