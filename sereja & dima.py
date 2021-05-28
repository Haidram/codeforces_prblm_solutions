n = int(input())
a = list(map(int,input().strip().split()))[:n]
b = list(reversed(a))
count_s = 0
count_d = 0
i = 0
j = 0
while i+j < n:
    if (i+j)%2 == 0:
        if a[i]>=b[j]:
            count_s += a[i]
            i += 1
        else:
            count_s += b[j]
            j += 1
    else:
        if a[i]>=b[j]:
            count_d += a[i]
            i += 1
        else:
            count_d += b[j]
            j += 1
print("{} {}".format(count_s,count_d))
