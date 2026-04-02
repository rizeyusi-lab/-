class Player:
    def __init__(self, name, ab, h):
        self.name = name
        self.ab = int(ab)
        self.h = int(h)

    def print(self):
        print(f"name:{self.name}, AVG:{self.getAVG():.3f}, AB:{self.ab}, H:{self.h}")

    def getAVG(self):
        return self.h / self.ab


for i in range(2):
    name, ab, h = input().split()
    P = Player(name, ab, h)
    P.print()