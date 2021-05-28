def minProduct(numArray):
    a = numArray[0]
    b = numArray[1]
    x = numArray[2]
    y = numArray[3]
    n = numArray[4]
    minProd = a*b
    if a+b <= x+y+n:
        a = x
        b = y
        if minProd > a*b:
            minProd = a*b
    elif a == b and a+b > x+y+n:
        if x<=y and a-x<n:
            d = a-x
            a = x
            b = b-(n-d)
            if minProd > a*b:
                minProd = a*b
        elif x<=y and a-x>=n:
            a = a-n
            if minProd > a*b:
                minProd = a*b
        elif y<x and b-y<n:
            d = b-y
            b = y
            a = a-(n-d)
            if minProd > a*b:
                minProd = a*b
        elif y<x and b-y>=n:
            b = b-n
            if minProd > a*b:
                minProd = a*b
    elif a>b and b-y>=n:
        b = b-n
        if minProd > a*b:
            minProd = a*b
    elif a<b and a-x>=n:
        a = a-n
        if minProd > a*b:
            minProd = a*b
    else:
        if a>b and a-x>=n:
            d = b-y
            temp1 = y
            temp2 = a-(n-d)
            if minProd > temp1*temp2:
                minProd = temp1*temp2
            a = a-n
            if minProd > a*b:
                minProd = a*b
        elif a>b and a-x<n:
            e = a-x
            temp1 = x
            temp2 = b-(n-e)
            if minProd > temp1*temp2:
                minProd = temp1*temp2
            f = b-y
            b = y
            a = a-(n-f)
            if minProd > a*b:
                minProd = a*b
        elif a<b and b-y>=n:
            d = a-x
            temp1 = x
            temp2 = b-(n-d)
            if minProd > temp1*temp2:
                minProd = temp1*temp2
            b = b-n
            if minProd > a*b:
                minProd = a*b
        elif a<b and b-y<n:
            e = b-y
            temp1 = y
            temp2 = a-(n-e)
            if minProd > temp1*temp2:
                minProd = temp1*temp2
            f = a-x
            a = x
            b = b-(n-f)
            if minProd > a*b:
                minProd = a*b
    return minProd
num = int(input())
for i in range(num):
    m = []
    m = list(map(int,input().strip().split()))[:5]
    z = minProduct(m)
    print(z)
