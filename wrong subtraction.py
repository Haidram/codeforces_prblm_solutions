a = list(map(int,input().strip().split()))[:2]
num = a[0]
for i in range(a[1]):
    if num%10 == 0:
        num = int(num/10)
    else:
        num -= 1
print(num)
