N, M = map(int, input().split())

lst = list()
for row in range(N):
    lst.append(0)

for _ in range(M):
    i, j, k = map(int, input().split())
    
    for bsk in range(i - 1, j): 
        lst[bsk] = k

for a in lst:
    print(a, end=" ")