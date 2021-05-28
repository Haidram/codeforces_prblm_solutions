n = int(input())
a = input()
b = input()
count = 0
for i in range(n):
    temp = abs(int(a[i])-int(b[i]))
    count += min(temp,10-temp)
print(count)
