def solve(n, a):
    a = sorted(a)
    count = i = 0
    check = a[0]
    while i < n:
        if a[i] == check:
            count += 1
        else:
            break
        i += 1

    return n - count
    


t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int,input().strip().split()))[:n]
    print(solve(n, a))
