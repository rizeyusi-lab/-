n = int(input())

for _ in range(n):
    ox = input()
    total = 0
    count = 0

    for i in range(len(ox)):
        if ox[i] == "O":     
            count += 1
            total += count
        else:               
            count = 0

    print(total)             