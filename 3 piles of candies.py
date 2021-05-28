def findRes(a,b,c):
    num = a+b+c
    return num//2

q = int(input())
for i in range(q):
    arr = list(map(int,input().strip().split()))[:3]
    a = arr[0]
    b = arr[1]
    c = arr[2]
    result = findRes(a,b,c)
    print(result)
