n = int(input())
a = list(map(int,input().strip().split()))[:n]
maxNum = a[0]
minNum = a[0]
count = 0
for i in range(n):
    if a[i] > maxNum or a[i] < minNum:
        count += 1
        if a[i] > maxNum:
            maxNum = a[i]
        elif a[i] < minNum:
            minNum = a[i]
print(count)
