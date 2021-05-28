def solve(nk, s):
    n = nk[0]
    k = nk[1]

    if n < 2*k + 1:
        return 'NO'
    check = s[:k] + s[n-k:]
    if check == "".join(list(reversed(check))):
        return 'YES'
    return 'NO'


t = int(input())
for i in range(t):
    nk = list(map(int,input().strip().split()))[:2]
    s = input()
    print(solve(nk, s))
