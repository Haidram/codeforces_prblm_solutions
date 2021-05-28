n = int(input())
a = list(map(int,input().strip().split()))[:n]
count = 0
temp_off = 0
for i in range(n):
    if a[i] == -1 and temp_off >0:
        temp_off -= 1
    elif a[i] == -1 and temp_off == 0:
        count += 1
    elif a[i] > 0:
        temp_off += a[i]
print(count)
