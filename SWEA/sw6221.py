g = ["가위", "바위", "보"]
man1 = g.index(input())
man2 = g.index(input())

print(man1, man2)

if man1==man2:
    print(f"Result:Draw")
elif (man1==g.index("가위") and man2==g.index("보")) or (man1==g.index("바위") and man2==g.index("가위")) or (man1==g.index("보") and man2==g.index("바위")):
    print(f"Result:Man1 Win!")
else:
    print(f"Result:Man2 Win!")