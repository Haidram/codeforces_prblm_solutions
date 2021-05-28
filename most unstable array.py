t = int(input())
for i in range(t):
    a = list(map(int,input().strip().split()))[:2]
    n = a[0]
    m = a[1]
    if n == 0 or n == 1:
        print(0)
    elif n == 2:
        print(m)
    else:
        print(2*m)
