def solve(n, arr):
    arr.sort()
    cost = n*arr[0]
    for i in range(n):
        temp = (n-i)*arr[i]
        if temp > cost:
            cost = temp
    return cost


t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int,input().strip().split()))[:n]
    print(solve(n, arr))
