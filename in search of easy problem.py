num = int(input())
a = list(map(int,input().strip().split()))[:num]
count = 0
for i in range(num):
    if a[i] == 1:
        count +=1
if count >= 1:
    print("HARD")
else:
    print("EASY")
