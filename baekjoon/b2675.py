T = int(input())
#print(T)
for n in range(T):
    R, S = input().split() 
    #print(R, S)

    for i in S:
        for j in range(int(R)):
            print(i, end='')
    print()