def solve(n, b):
    count = 0
    val = False
    b.sort()
    flag1 = True
    
    for i in b:
        count += i

    if count-b[n+1] <= b[n+1]:
        flag1 = False

    if flag1:
        temp1 = count - b[n+1]
        i = 0
        while i < n+1:
            temp = temp1 - b[i]
            if temp < b[n+1]:
                break
            if temp == b[n+1]:
                val = True
                b.remove(b[n+1])
                b.remove(b[i])
                break
            i += 1

    if not val:
        count -= b[n+1]
        if count - b[n] == b[n]:
            val = True
            b.remove(b[n+1])
            b.remove(b[n])

    return val, b

t = int(input())
for i in range(t):
    n = int(input())
    b = list(map(int,input().strip().split()))[:n+2]
    value, result = solve(n, b)
    if not value:
        print("-1")
    else:
        j = 0
        while j<len(result):
            print(result[j], end=" ")
            j += 1
        print()
