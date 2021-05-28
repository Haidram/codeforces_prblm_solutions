a = list(map(int,input().strip().split()))[:2]
k = a[0]
r = a[1]
for i in range(1,11):
    checkval = k*i
    if checkval%10 == r or checkval%10 == 0:
        print(i)
        break
