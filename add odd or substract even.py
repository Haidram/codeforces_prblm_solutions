def pros(x,y):
    sum_arr = x+y
    if x<y:
        if sum_arr%2 == 0:
            return 2
        else:
            return 1
    elif y<x:
        if sum_arr%2 == 0:
            return 1
        else:
            return 2
    else:
        return 0

t = int(input())
for i in range(t):
    n = list(map(int,input().strip().split()))[:2]
    a = n[0]
    b = n[1]
    result = pros(a,b)
    print(result)
