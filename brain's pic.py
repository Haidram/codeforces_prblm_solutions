a = list(map(int,input().strip().split()))[:2]
m = a[0]
n = a[1]
x = ["0"]*m
check_arr = ['C','M','Y']
flag = 0
for i in range(m):
    x[i] = list(map(str,input().strip().split()))[:n]
for i in range(m):
    for j in range(n):
        if x[i][j] in check_arr:
            flag = 1
if flag == 1:
    print("#Color")
else:
    print("#Black&White")
