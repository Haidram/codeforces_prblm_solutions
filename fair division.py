def solve(n, a):
    count = 0
    a = list(sorted(a, reverse=True))
    for i in a:
        if count > 0:
            count -= i
        else:
            count += i

    if n == 1 or count != 0:
        return 'NO'
    return 'YES'


t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int,input().strip().split()))[:n]
    print(solve(n, a))
