a = []

while True:
    n = int(input())
    if n ==-1:
        break
    a.append(n)

result = a[-3:]

for x in result:
    print(x, end=' ')
