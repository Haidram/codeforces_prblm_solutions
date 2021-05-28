a = list(map(int,input().strip().split()))[:8]
n = a[0]
k = a[1]
l = a[2]
c = a[3]
d = a[4]
p = a[5]
nl = a[6]
np = a[7]
drink = k*l
lime = c*d
temp1 = drink//(nl*n)
temp2 = lime//n
temp3 = p//(np*n)
print(min(temp1,temp2,temp3))
