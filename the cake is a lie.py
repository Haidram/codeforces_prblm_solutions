def solve(arr):
    n = arr[0]
    m = arr[1]
    k = arr[2]
    if k == (n*m)-1:
        return "YES"
    else:
        return "NO"

t = int(input())
for i in range(t):
    arr = list(map(int,input().strip().split()))[:3]
    print(solve(arr))
