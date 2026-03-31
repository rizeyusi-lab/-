class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def print(self):
        isOld = 'child'
        if int(age) >= 18:
            isOld = 'adult'
        else:
            isOld = 'child'

        print(f"{name}({age}) : {isOld}")
    
for x in range(2):
    name, age = input().split()
    obj = Person(name, age)
    obj.print()