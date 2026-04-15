S = int(input())
E = int(input())

if S<E:
    for i in range(1, 10): 
        for x in range(S, E+1):  
            print(f"{x} * {i} = {i*x}   ", end='')
        print()
else:
    for i in range(1, 10): 
        for x in range(S, E-1, -1):  
            print(f"{x} * {i} = {i*x}   ", end='')
        print()