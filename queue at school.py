a = list(map(int,input().strip().split()))[:2]
b = ""
b = input()
b = list(b)
for i in range(a[1]):
    j = 0
    while j < a[0]-1:
        if b[j] == 'B' and b[j+1] == 'G':
            x = b[j]
            b[j] = b[j+1]
            b[j+1] = x
            j += 2
        else:
            j += 1
b = "".join(b)      
print(b)
