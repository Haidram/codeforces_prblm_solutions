t = int(input())
for i in range(t):
    a = list(map(int,input().strip().split()))[:3]
    x = a[0]
    y = a[1]
    n = a[2]
    temp_n = n - y
    temp = temp_n%x
    print(n-temp)
