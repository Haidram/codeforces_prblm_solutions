def do_it(a, b):
    m = len(a)
    n = len(b)
    sub = [[0 for k in range(m+1)] for l in range(n+1)]
    for i in range(n+1):
        for j in range(m+1):
            if i == 0 or j == 0:
                sub[i][j] = 0
            else:
                if a[j-1] == b[i-1]:
                    sub[i][j] = sub[i-1][j-1] + 1
                else:
                    sub[i][j] = 0
    max_num = 0
    for i in range(n+1):
        for j in range(m+1):
            if sub[i][j] > max_num:
                max_num = sub[i][j]
    return (m+n)-(2*max_num)

t = int(input())
for i in range(t):
    a = input()
    b = input()
    print(do_it(a, b))
