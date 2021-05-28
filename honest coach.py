t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int,input().strip().split()))[:n]
    a.sort()
    min_diff = abs(a[0]-a[1])
    for j in range(n-1):
        if min_diff > abs(a[j]-a[j+1]):
            min_diff = abs(a[j]-a[j+1])
    print(min_diff)
