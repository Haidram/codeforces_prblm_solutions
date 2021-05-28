n = list(map(int,input().strip().split()))[:2]
a = n[0]
b = n[1]
if a<b:
    print(a,end = " ")
else:
    print(b,end = " ")
print(int(abs(a-b)/2))
