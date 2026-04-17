a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
print(f"[{a}, {b}, {c}, {d}, {e}]")
print(f"{a} {b} {c} {d} {e}")
# -----------------------------------------
lst = []

for i in range(5):
    inp=int(input())
    lst.append(inp)

print(lst)
for i in lst:
    print(i, end=' ')