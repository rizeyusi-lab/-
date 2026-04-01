class Soccer:
    def __init__(self, name, score):
        self.name = name
        self.wp = score
    def print_info(self):
        print(self.name, self.score)

N, M = map(int, input().split())
lst = []
res = []
for i in range(N):
    name, score = input().split()
    # print(team_name, wp)
    lst.append(Soccer(name, score))

# for j in range(len(lst)):
#     lst[j].print_info()

for k in range(len(lst)):
    if int(lst[k].wp) >= M:
        res.append(lst[k].name)

# print(res)
for x in range(len(res)-1, -1, -1):
    print(res[x])