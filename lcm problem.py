t = int(input())
for i in range(t):
    a = list(map(int,input().strip().split()))[:2]
    l = a[0]
    r = a[1]
    if 2*l <= r:
        print("{} {}".format(l,2*l))
    else:
        print("-1 -1")
