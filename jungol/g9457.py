K = int(input())

def get_diff(n):
    return abs(K-n)

a, b, c = map(int,input().split())

print(get_diff(a))
print(get_diff(b))
print(get_diff(c))