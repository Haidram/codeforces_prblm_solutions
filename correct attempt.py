def writeSol(intArray):
    countNum = 0
    for num in range(3):
        if intArray[num] == 1:
            countNum += 1
    if countNum >=2:
        return 1
    else:
        return 0
        
a = int(input())
count = 0
for i in range(a):
    b = list(map(int,input().strip().split()))[:3]
    count += writeSol(b)
    
print(count)
