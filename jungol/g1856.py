n, m = map(int, input().split())
a = 0
for i in range(n):
    if i%2==0:
        if i>0: a += m
        for j in range(m):
            a += 1
            print(a, end=" ")
    else:
        a += m
        for j in range(m):
            print(a, end=" ")
            a -= 1
    print()
