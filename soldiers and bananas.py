a = list(map(int,input().strip().split()))[:3]

k = a[0]
n = a[1]
w = a[2]

num = int(((w*(w+1)*k)/2)-n)
if num > 0:
    print(num)
else:
    print("0")
