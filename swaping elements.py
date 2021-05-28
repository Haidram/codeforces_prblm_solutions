t = int(input())
for i in range(t):
    num = list(map(int,input().strip().split()))[:2]
    n = num[0]
    k = num[1]
    a = sorted(list(map(int,input().strip().split()))[:n])
    b = sorted(list(map(int,input().strip().split()))[:n],reverse = True)
    count = 0
    for i in range(n):
        if i < k and a[i] < b[i]:
            count += b[i]
        else:
            count += a[i]
    print(count) 
