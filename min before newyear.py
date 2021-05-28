t = int(input())
for i in range(t):
    a = list(map(int,input().strip().split()))[:2]
    h = a[0]
    m = a[1]
    temp = 24*60 - (h*60 + m)
    print(temp)
