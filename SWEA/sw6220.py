T = int(input())
for test_case in range(1, T + 1 ):
    ch = input()
    if ch.islower():
        print(f"#{test_case} {ch} 는 소문자 입니다.")
    else:
        print(f"#{test_case} {ch} 는 대문자 입니다.")

