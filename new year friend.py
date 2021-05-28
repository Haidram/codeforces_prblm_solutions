a = list(map(int,input().strip().split()))[:3]
for i in range(3):
    for j in range(2-i):
        if a[j] > a[j+1]:
            temp = a[j]
            a[j] = a[j+1]
            a[j+1] = temp
print(abs(a[0]-a[2]))
