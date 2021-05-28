def gcd(x,y):
    if x>y:
        if y == 0:
            return x
        else:
            return gcd(y,x%y)
    else:
        if x == 0:
            return y
        else:
            return gcd(x,y%x)

arr = list(map(int,input().strip().split()))[:3]
a = arr[0]
b = arr[1]
n = arr[2]
temp = n
i = 0
while True:
    if i%2 == 0:
        take = gcd(a,temp)
        if take > temp:
            print(1)
            break
        temp -= take
    else:
        take = gcd(b,temp)
        if take > temp:
            print(0)
            break
        temp -= take
    i += 1
