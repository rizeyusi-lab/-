n,m = map(int, input().split())

num = 1

for a in range(n):
    for b in range(m):
        print(num, end=' ')
        num += 1  
    print()