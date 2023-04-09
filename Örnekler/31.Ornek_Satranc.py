class spot:
    def __init__(self,k_sayi,k_harf,color,piece):
        self.sayı = k_sayi
        self.harf = k_harf
        self.color = color
        self.piece = piece

class tas(object):
    def __init__(self,color,piece):
        self.color = color
        self.symbol = None
class piyon(tas):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = "♟" if color == "black" else "♙"

class tahta:
    def __init__(self):
        self.spots = []
        for i in range(8):
            for j in range(8):
                if ( i + j ) % 2 ==0:
                    color = "white"
                else:
                    color = "black"
                self.spots.append(spot(i , j , color , " "))




    def yazdir(self):
        for i in range(8):
            for j in range(8):
                    if self.spots[i*8+j].color == "white":
                        print(f"\033[48;5;255m\033[30m {self.spots[i*8+j].piece} ",end=" ")
                    else:
                        print(f"\033[48;5;245m\033[30m {self.spots[i*8+j].piece} ", end=" ")
            print("\033[0m")



bord = tahta()
print("")
bord.yazdir()