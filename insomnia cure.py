a = [0]*5
for i in range(5):
    a[i] = int(input())
k = a[0]
l = a[1]
m = a[2]
n = a[3]
d = a[4]
count = 0
for j in range(1,d+1):
    if j%k != 0 and j%l != 0 and j%m != 0 and j%n != 0:
        count += 1
print(d-count)
