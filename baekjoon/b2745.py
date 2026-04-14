N, B = input().split()

res = 0
for idx, ch in enumerate(N):
    if ch.isdigit():
        res += int(ch) * (int(B) ** (len(N) - 1 - idx))
    else:
        res += (ord(ch) - 55) * (int(B) ** (len(N) - 1 - idx))
print(res) 

