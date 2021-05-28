n = int(input())
t = list(map(int,input().strip().split()))[:n]
num1 = 0
num2 = 0
num3 = 0
a1 = []
a2 = []
a3 = []
for i in range(n):
    if t[i] == 1:
        num1 += 1
        a1.append(i+1)
    elif t[i] == 2:
        num2 += 1
        a2.append(i+1)
    else:
        num3 += 1
        a3.append(i+1)
num_temp = min(num1,num2)
num = min(num_temp,num3)
print(num)
if num != 0:
    for i in range(num):
        print("{} {} {}".format(a1[i],a2[i],a3[i]))
