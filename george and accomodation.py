num = int(input())
count = 0
for i in range(num):
    a = []
    a = list(map(int,input().strip().split()))[:2]
    diff = abs(a[0]-a[1])
    if diff >= 2:
        count += 1
print(count)
