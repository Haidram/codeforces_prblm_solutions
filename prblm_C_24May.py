def solve(n, lr, uv):
    


t = int(input())
for i in range(t):
    n = int(input())
    lr = []
    uv = []
    for j in range(n):
        temp = list(map(int,input().strip().split()))[:2]
        lr.append(temp)
    for k in range(n-1):
        temp = list(map(int,input().strip().split()))[:2]
        uv.append(temp)
    print(solve(n, lr, uv))
