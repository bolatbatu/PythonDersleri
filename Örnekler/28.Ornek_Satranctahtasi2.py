class Tas:
    def __init__(self, renk, sembol):
        self.renk = renk
        self.simbol = sembol
        
class Piyon(Tas):
    def __init__(self, renk):
        super().__init__(renk, "\033[30m♟")
class Piyon2(Tas):
    def __init__(self, renk):
       super().__init__(renk, "♙")

class Vezir(Tas):
    def __init__(self, renk):
        super().__init__(renk, "\033[30m♛")

class Vezir2(Tas):
    def __init__(self, renk):
        super().__init__(renk, "♛")

class Sah(Tas):
    def __init__(self, renk):
        super().__init__(renk, "\033[30m♚")

class Sah2(Tas):
    def __init__(self, renk):
        super().__init__(renk, "♔")

class Kale(Tas):
    def __init__(self, renk):
        super().__init__(renk, "\033[30m♜")

class Kale2(Tas):
    def __init__(self, renk):
        super().__init__(renk, "♖")

class Fil(Tas):
    def __init__(self, renk):
        super().__init__(renk, "\033[30m♝")

class Fil2(Tas):
    def __init__(self, renk):
        super().__init__(renk, "♗")

class At(Tas):
    def __init__(self, renk):
        super().__init__(renk, "\033[30m♞")

class At2(Tas):
    def __init__(self, renk):
        super().__init__(renk, "♘")       
         
class SatrancTahtasi:
    def __init__(self):
        self.taslar = {}
        self.yeni_oyun()
        
    def yeni_oyun(self):
        self.taslar = {}
        self.taslar[(0,4)] = Vezir("siyah")
        self.taslar[(0,3)] = Sah("siyah")
        self.taslar[(0,7)] = Kale("siyah")
        self.taslar[(0,0)] = Kale("siyah")
        self.taslar[(0,5)] = Fil("siyah")
        self.taslar[(0,2)] = Fil("siyah")        
        self.taslar[(0,1)] = At("siyah")
        self.taslar[(0,6)] = At("siyah")
        self.taslar[(1,0)] = Piyon("siyah")
        self.taslar[(1,1)] = Piyon("siyah")
        self.taslar[(1,2)] = Piyon("siyah")
        self.taslar[(1,3)] = Piyon("siyah")
        self.taslar[(1,4)] = Piyon("siyah")
        self.taslar[(1,5)] = Piyon("siyah")
        self.taslar[(1,6)] = Piyon("siyah")
        self.taslar[(1,7)] = Piyon("siyah")
        #Beyaz------------------------------------------------
        self.taslar[(7,4)] = Vezir2("beyaz")
        self.taslar[(7,3)] = Sah2("beyaz")
        self.taslar[(7,7)] = Kale2("beyaz")
        self.taslar[(7,0)] = Kale2("beyaz")
        self.taslar[(7,5)] = Fil2("beyaz")
        self.taslar[(7,2)] = Fil2("beyaz")        
        self.taslar[(7,1)] = At2("beyaz")
        self.taslar[(7,6)] = At2("beyaz")
        self.taslar[(6,0)] = Piyon2("beyaz")
        self.taslar[(6,1)] = Piyon2("beyaz")
        self.taslar[(6,2)] = Piyon2("beyaz")
        self.taslar[(6,3)] = Piyon2("beyaz")
        self.taslar[(6,4)] = Piyon2("beyaz")
        self.taslar[(6,5)] = Piyon2("beyaz")
        self.taslar[(6,6)] = Piyon2("beyaz")
        self.taslar[(6,7)] = Piyon2("beyaz")
        
        
    def tas_konumu(self, x, y):
        if (x, y) in self.taslar:
            return self.taslar[(x, y)]
        else:
            return None
        
    def tahta_yazdir(self):
        for i in range(8):
            for j in range(8):
                if (i+j) % 2 == 0:
                    print(" \033[47m  ", end="")
                else:
                    print(" \033[40m  ", end="")
                tas = self.tas_konumu(i, j)
                if tas is not None:
                    print(tas.simbol, end="")
                else:
                    print(" ", end="")
            print(" \033[0m")
tahta = SatrancTahtasi()
tahta.tahta_yazdir()
