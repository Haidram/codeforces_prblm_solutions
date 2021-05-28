def isDistinct(year):
    year = str(year)
    count = 0
    a = [0]*10
    for i in range(len(year)):
        a[int(year[i])-1] += 1
    for j in range(10):
        if a[j] == 1:
            count += 1
    if count == len(year):
        return True
    else:
        return False
        
num = int(input())
i = 0
num = num + 1
while not isDistinct(num):
    num += 1
print(num)
    
