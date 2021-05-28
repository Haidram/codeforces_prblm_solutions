a = list(map(int,input().strip().split()))[:2]
b = list(map(int,input().strip().split()))[:a[0]]

winnerScore = b[a[1]-1]
winnerCount = 0
errorNum = len(b)
for i in range(len(b)):
    if b[i] == 0:
        errorNum -= 1

if errorNum == 0:
    print("0")
else:
    for j in range(len(b)):
        if b[j] >= winnerScore and b[j] != 0:
            winnerCount += 1
    print(winnerCount)
