n = int(input())  
data = list(map(int, input().split())) 

for i in range(0, n - 1):
    
    min_index = i 
    
    for j in range(i + 1, n):
        if data[j] < data[min_index]:
            min_index = j 
            
    temp = data[i]
    data[i] = data[min_index]
    data[min_index] = temp
    
    for num in data:
        print(num, end=" ")
    print() 