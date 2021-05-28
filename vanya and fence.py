num = list(map(int,input().strip().split()))[:2]
heightArray = list(map(int,input().strip().split()))[:num[0]]
hMax = num[1]

count = 0
for i in range(len(heightArray)):
    if heightArray[i] <= hMax:
        count += 1
    else:
        count += 2
print(count)
