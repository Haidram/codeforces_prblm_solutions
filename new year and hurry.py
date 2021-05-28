a = list(map(int,input().strip().split()))[:2]
n = a[0]
k = a[1]
checkvalue = (480-2*k)/5
i = 1
while i*(i+1) <= checkvalue and i <= n:
    i += 1
print(i-1)
