class Health:
    def __init__(self, height, weight):
        self.height = int(height)
        self.weight = weight
    def print_var(self):
            print(f'키:{self.height:d} 몸무게:{self.weight:.1f}')

h1, w1 = map(float,input('당신의 키와 몸무게를 입력하세요.').split())
p1 = Health(h1, w1)
p1.print_var()
h2, w2 = map(float,input('친구의 키와 몸무게를 입력하세요').split())
p2 = Health(h2, w2)
p2.print_var()

print('my', end=' ')
p1.print_var()
print('friend', end=' ')
p2.print_var()

print('plus 키:', p1.height + p2.height,',몸무게:', p1.weight + p2.weight)
print('minus 키:', {abs(p1.height - p2.height)}, ',몸무게:')