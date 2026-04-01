n1, n2 = map(int, input().split())
# print(n1, n2)

def func_plus(p1, p2):
    return p1 + p2

ret1 = func_plus(n1, n2)
print(f"두 수의 합 = {ret1}")

def func_minus(p1, p2):
    if p1>p2:
        return p1-p2
    else:
        return p2-p1

ret2 = func_minus(n1, n2)
print(f"두 수의 차 = {ret2}")