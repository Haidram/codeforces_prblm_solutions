a= list(map(int,input().strip().split()))[:2]
n = a[0]
k = a[1]
b = list(map(int,input().strip().split()))[:n]
count = 0
for data in b:
    if data + k <= 5:
        count += 1
print(count//3)
