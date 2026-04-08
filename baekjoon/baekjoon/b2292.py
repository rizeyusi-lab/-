N = int(input())
boundary = 1 
x = 1

while True:
    if N<= boundary:
        break
    boundary = boundary + (6*x)
    x = x + 1
    # print(x, boundary)

print(x) 