n = int(input())
a = list(map(int,input().strip().split()))[:n]
max_a = a[0]
index_max = 0
min_a = a[0]
index_min = 0
for i in range(n):
    if max_a < a[i]:
        max_a = a[i]
        index_max = i
    if min_a >= a[i]:
        min_a = a[i]
        index_min = i
count = 0
if index_max <= index_min:
    count += (index_max) + (n-1-index_min)
else:
    count += (index_max) + (n-1-index_min-1)
print(count)
