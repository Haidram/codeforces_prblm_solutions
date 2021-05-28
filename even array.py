t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int,input().strip().split()))[:n]
    o_err = 0
    e_err = 0
    for j in range(n):
        if j%2 == 0:
            if a[j]%2 == 1:
                e_err += 1
        else:
            if a[j]%2 == 0:
                o_err += 1
    if o_err != e_err:
        print("-1")
    else:
        print(o_err)
