num1, num2 = 0, 0

def process():
    global num1, num2
    if num1 > num2:
        num1 //= 2
        num2 *= 2
    elif num2 > num1:
        num2 //= 2
        num1 *= 2

num1, num2 = map(int, input().split())
process()
print(num1, num2)