N = int(input())
for i in range(N,0,-1):
    print(i, end=' ')

lst = []
N = int(input())
for i in range(1, N+1):
    lst.append(i)
lst2 = list(reversed(lst))
print(*lst2, end = ' ')