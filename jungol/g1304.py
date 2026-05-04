n=int(input())

a = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        print(i + a, end=" ")
        a += n
    print()
    a = 0