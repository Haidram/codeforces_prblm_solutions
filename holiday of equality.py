n = int(input())
a = list(map(int,input().strip().split()))[:n]
max_a = a[0]
for data in a:
    if data > max_a:
        max_a = data
count = 0
for i in range(n):
    count += max_a-a[i]
print(count)
