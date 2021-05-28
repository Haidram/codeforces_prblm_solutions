num = int(input())
a = [0]*num
for i in range(num):
    a[i] = int(input())
count = 1
for j in range(i):
    if a[j] != a[j+1]:
        count +=1
        
print(count)
