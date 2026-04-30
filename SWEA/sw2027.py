print(f"#++++")
print(f"+#+++")
print(f"++#++")
print(f"+++#+")
print(f"++++#")


#-------------------

for row in range(5):
    for col in range(5):
        if row==col:
            print('#', end="")
        else:
            print('+', end="")
    print()