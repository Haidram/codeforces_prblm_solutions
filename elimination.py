def solve(abcd):
    a = abcd[0]
    b = abcd[1]
    c = abcd[2]
    d = abcd[3]

    return max(a+b, c+d)


t = int(input())
for i in range(t):
    abcd = list(map(int,input().strip().split()))[:4]
    print(solve(abcd))
