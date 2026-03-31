class Building:
    def __init__(self, year, price):
        self.year = year
        self.price = price
    def print_building(self):
        print(self.year, self.price)

blst = []

N = int(input())
for i in range(N):
    year, price = map(int, input().split())
    b = Building(year, price)
    blst.append(b)

Y, P = map(int, input().split())

for k in range(N):
    if blst[k].year >= Y and blst[k].price <= P:
        blst[k].print_building()
  

