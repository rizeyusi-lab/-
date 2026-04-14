class one:
    def __init__(self, name, age):
        self.name = name
        self.age = age

name, age = input().split()
O = one(name, age)

print(f'My name is {O.name}.')
print(f'I am {O.age} years old.')












