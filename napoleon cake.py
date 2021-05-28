def solve(n, arr):
    arr.reverse()
    power = 0
    s = []
    for i in arr:
        if i > power:
            power = i
        if power > 0:
            s.append('1')
            power -= 1
        else:
            s.append('0')

    s.reverse()
    return " ".join(s)


t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int,input().strip().split()))[:n]
    print(solve(n, arr))
