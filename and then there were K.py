def solve(n):
    len_n = len(bin(n)) - 2
    if len_n > 1:
        s = "".join(['1']*(len_n-1))
        ans = int(s,2)
    else:
        ans = 0
    return ans

t = int(input())
for i in range(t):
    n = int(input())
    result = solve(n)
    print(result)
