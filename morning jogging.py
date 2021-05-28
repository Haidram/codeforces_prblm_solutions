def solve(arr, n, m):
    b = []

    for i in range(n):
        b = b + arr[i]

    b.sort()
    c = [[-1 for i in range(m)] for j in range(n)]

    for i in range(m):
        for j in range(n):
            if b[i] in arr[j]:
                c[j][i] = b[i]
                arr[j].remove(b[i])
                break

    x = 0
    while x < n:
        ind_c = ind_arr = 0
        while ind_arr <= len(arr[x])-1:
            if c[x][ind_c] == -1:
                c[x][ind_c] = arr[x][ind_arr]
                ind_c += 1
                ind_arr += 1
            else:
                ind_c += 1
        x += 1
        
    return c

t = int(input())
for i in range(t):
    a = list(map(int,input().strip().split()))[:2]
    n = a[0]
    m = a[1]
    arr = []
    for j in range(n):
        b = list(map(int,input().strip().split()))[:m]
        arr.append(b)
    result = solve(arr, n, m)
    for k in range(n):
        s = ""
        for l in range(m):
            if l != m-1:
                s = s + str(result[k][l]) + " "
            else:
                s = s + str(result[k][l])
        print(s)
