class PersonAge:
    def __init__(self, name, age):
        self.name = name
        self.age = int(age)

N = int(input())
# print(N)
people = [PersonAge(*input().split()) for i in range(N)]

people.sort(key=lambda x: x.age, reverse=True)

for p in people:
    print(f"Name:{p.name}, Age:{p.age}")