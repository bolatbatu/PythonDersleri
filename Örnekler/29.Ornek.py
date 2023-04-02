class Tahta:
    def __init__(self):
        self.taslar = [[None for j in range(8)] for i in range(8)]
        self.piyanlar = []
        for i in range(8):
            piyon = Piyon("beyaz", i, 1)
            self.taslar[i][1] = piyon
            self.piyanlar.append(piyon)
            piyon = Piyon("siyah", i, 6)
            self.taslar[i][6] = piyon
            self.piyanlar.append(piyon)

    def goster(self):
        print("  A B C D E F G H ")
        print(" +----------------+ ")
        for y in range(8):
            print(str(8 - y) + "|", end="")
            for x in range(8):
                tas = self.taslar[x][7 - y]
                if tas is None:
                    if (x + y) % 2 == 0:
                        print("  ", end="")
                    else:
                        print("##", end="")
                else:
                    print(tas.gorunum(), end="")
            print("|" + str(8 - y))
        print(" +----------------+ ")
        print("  A B C D E F G H ")

    def hareket(self, x1, y1, x2, y2):
        if x1 < 0 or x1 > 7 or y1 < 0 or y1 > 7 or x2 < 0 or x2 > 7 or y2 < 0 or y2 > 7:
            print("Geçersiz hareket!")
            return

        tas = self.taslar[x1][y1]
        if tas is None:
            print("Geçersiz hareket!")
            return

        if not tas.hareket_gecerli(x1, y1, x2, y2, self.taslar):
            print("Geçersiz hareket!")
            return

        self.taslar[x1][y1] = None
        self.taslar[x2][y2] = tas
        tas.x = x2
        tas.y = y2
        self.goster()


class Piyon:
    def __init__(self, renk, x, y):
        self.renk = renk
        self.x = x
        self.y = y

    def gorunum(self):
        if self.renk == "beyaz":
            return " P"
        else:
            return " p"

    def hareket_gecerli(self, x1, y1, x2, y2, taslar):
        if self.renk == "beyaz":
            dy = y2 - y1
            if dy != 1:
                return False
        else:
            dy = y1 - y2
            if dy != 1:
                return False

        dx = abs(x2 - x1)
        if dx == 0:
            if taslar[x2][y2] is not None:
                return False
        elif dx == 1:
            if taslar[x2][y2] is None:
                return False
            if taslar[x2][y2].renk == self.renk:
                return False
        else:
           
class Piyon:
    def __init__(self, renk, x, y):
        self.renk = renk
        self.x = x
        self.y = y
        self.ilk_hamle = True

    def gorunum(self):
        if self.renk == "beyaz":
            return " P"
        else:
            return " p"

    def hareket_gecerli(self, x1, y1, x2, y2, taslar):
        if self.renk == "beyaz":
            dy = y2 - y1
            if dy < 1:
                return False
        else:
            dy = y1 - y2
            if dy < 1:
                return False

        dx = abs(x2 - x1)
        if dx == 0:
            if taslar[x2][y2] is not None:
                return False
        elif dx == 1:
            if taslar[x2][y2] is None:
                return False
            if taslar[x2][y2].renk == self.renk:
                return False
        else:
            return False

        if self.ilk_hamle:
            if dx == 0 and dy == 2:
                if self.renk == "beyaz":
                    if taslar[x1][y1 + 1] is not None:
                        return False
                else:
                    if taslar[x1][y1 - 1] is not None:
                        return False
            elif dx == 1 and dy == 1:
                if taslar[x2][y2] is None:
                    return False

        self.ilk_hamle = False
        return True
class Tahta:
    def __init__(self):
        self.taslar = [[None for j in range(8)] for i in range(8)]
        self.piyanlar = []
        for i in range(8):
            piyon = Piyon("beyaz", i, 1)
            self.taslar[i][1] = piyon
            self.piyanlar.append(piyon)
            piyon = Piyon("siyah", i, 6)
            self.taslar[i][6] = piyon
            self.piyanlar.append(piyon)

    def goster(self):
        print("  A B C D E F G H ")
        print(" +----------------+ ")
        for y in range(8):
            print(str(8 - y) + "|", end="")
            for x in range(8):
                tas = self.taslar[x][7 - y]
                if tas is None:
                    if (x + y) % 2 == 0:
                        print("  ", end="")
                    else:
                        print("##", end="")
                else:
                    print(tas.gorunum(), end="")
            print("|" + str(8 - y))
        print(" +----------------+ ")
        print("  A B C D E F G H ")

    def hareket(self, x1, y1, x2, y2):
        if x1 < 0
