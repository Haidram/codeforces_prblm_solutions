def solve(n, a):
    if n == 1:
        if a[0]%2 == 0:
            return 1, 1
        else:
            return -1, a
        
    count = 0
    ind = []
    for i in range(n):
        count += a[i]
        ind.append(str(i+1))

    if count%2 == 0:
        return n, " ".join(ind)

    for i in range(n):
        if a[i]%2 == 1:
            ind.pop(i)
            break

    return n-1, " ".join(ind)


t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int,input().strip().split()))[:n]
    ans, result = solve(n, a)
    print(ans)
    if ans != -1:
        print(result)
