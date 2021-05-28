def codepro(a,b,n):
    count = 0
    while a <= n and b <= n:
        if a>b:
            b += a
        else:
            a += b
        count += 1
    return count

t = int(input())
for i in range(t):
    arr = list(map(int,input().strip().split()))[:3]
    a = arr[0]
    b = arr[1]
    n = arr[2]
    result = codepro(a,b,n)
    print(result)
