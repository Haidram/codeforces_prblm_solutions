def numAdd(x,y):
    if x<y:
        return y-x
    elif x%y != 0:
        m = x%y
        return y-m
    else:
        return 0

n = int(input())
for i in range(n):
    a = list(map(int,input().strip().split()))[:2]
    leastNum = numAdd(a[0],a[1])
    print(leastNum)
