n = int(input())

for i in range(1, n + 1):
    numbers = map(int, input().split())

    answer = sum(n for n in numbers if n % 2 != 0)
    print(f"#{i} {answer}")

    