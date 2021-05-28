def solve(n, k):
    num = n**k
    ans = num%(10**9 +7)
    return ans

t = int(input())
for i in range(t):
    a = list(map(int,input().strip().split()))[:2]
    n = a[0]
    k = a[1]
    result = solve(n, k)
    print(result)
