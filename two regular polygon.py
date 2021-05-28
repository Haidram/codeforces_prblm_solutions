def findAns(n,m):
    rem = n-m
    if rem%m == 0:
        return "YES"
    else:
        return "NO"

t = int(input())
for i in range(t):
    arr = list(map(int,input().strip().split()))[:2]
    n = arr[0]
    m = arr[1]
    result = findAns(n,m)
    print(result)
