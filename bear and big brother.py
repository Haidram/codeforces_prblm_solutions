w = list(map(int,input().strip().split()))[:3]
a = w[0]
b = w[1]
flag = 0
i = 0
while flag == 0:
    if a <= b:
        a *= 3
        b *= 2
        i += 1
    else:
        flag = 1
        
print(i)
