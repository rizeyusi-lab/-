a = input()
print(*a [::2])

a = input()
for i in range(len(a)):
    if i%2==0:
        print(a[i], end=' ')