n = list(map(int,input().strip().split()))[:4]
maxNum = n[0]
for i in range(len(n)):
    if n[i] > maxNum:
        maxNum = n[i]
for j in range(len(n)):
    if maxNum - n[j] != 0:
        print(maxNum-n[j],end=" ")
