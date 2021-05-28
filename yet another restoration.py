def find_ans(n,x,y):
    a = []
    a.append(str(y))
    d = y-x
    num = 0
    j = n-2
    rem = n
    while j+1 > 0:
        if d%(j+1) == 0:
            num = j
            rem = n - 2 - num
            break
        else:
            j -= 1
    diff = d//(num+1)
    for k in range(num+1):
            a.append(str(x+(k*diff)))
    i = 1
    while rem>0:
        if x-(i*diff) > 0:
            a.append(str(x-(i*diff)))
        else:
            break
        rem -= 1
        i += 1
    j = 1
    while rem>0:
        a.append(str(y+(j*diff)))
        rem -= 1
        j += 1
    b = " ".join(a)
    return b
        
t = int(input())
for i in range(t):
    arr = list(map(int,input().strip().split()))[:3]
    n = arr[0]
    x = arr[1]
    y = arr[2]
    result = find_ans(n,x,y)
    print(result)
