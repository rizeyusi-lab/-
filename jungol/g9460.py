a, b = map(int, input().split())
def swap_local(a, b):
    a, b = b, a
    print(f"함수 내부: a = {a}, b = {b}")

def swap_global():
    global a, b
    a, b = b, a
    print(f"함수 내부: a = {a}, b = {b}")

swap_local(a, b)
print(f"함수 외부: a = {a}, b = {b}")

swap_global()
print(f"함수 외부: a = {a}, b = {b}")