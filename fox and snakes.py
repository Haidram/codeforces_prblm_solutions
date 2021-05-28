n = list(map(int,input().strip().split()))[:2]
rowN = n[0]
colN = n[1]
s1 = ""
s2 = ""
s3 = "#"
for i in range(colN):
    s1 += "#"
for j in range(colN-1):
    s2 += "."
    
for i in range(1,rowN+1):
    if i%4 == 1 or i%4 == 3:
        print(s1)
    if i%4 == 2:
        print(s2+s3)
    if i%4 == 0:
        print(s3+s2)
