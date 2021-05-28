def solve(n, x):
    x[-1] += 1
    x = list(reversed(x))
    for i in range(1,n):
        if x[i]+1 >= x[i-1]:
            continue
        else:
            x[i] += 1
    return len(list(set(x)))


t = int(input())
for i in range(t):
    n = int(input())
    x = list(map(int,input().strip().split()))[:n]
    print(solve(n, x))
