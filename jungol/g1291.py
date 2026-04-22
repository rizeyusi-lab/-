while True:
    a, b = map(int, input().split())
    if 2 <= a <= 9 and 2 <= b <= 9:
        step = 1 if a <= b else -1
        gugudan = range(a, b + step, step)
        
        for i in range(1, 10):
            line = [f"{nums} * {i} = {nums * i:2d}" for nums in gugudan]
            print("   ".join(line))
        break
    else:
        print("INPUT ERROR!")