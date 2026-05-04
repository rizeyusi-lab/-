name=input()
age=int(input())

print(f"{name}(은)는 2099년에 100세가 될 것입니다.")

#-----------------------------------
name, age = input(), int(input())
base_year = 2019

result_year = base_year + (100 - age)

output = "{}(은)는 {}년에 100세가 될 것입니다.".format(name, result_year)
print(output)