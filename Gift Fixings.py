def findSteps(x,y):
    min_a = a[0]
    min_b = b[0]
    count = 0
    for i in range(len(a)):
        if a[i] < min_a:
            min_a = a[i]
        if b[i] < min_b:
            min_b = b[i]
    for i in range(len(a)):
        if a[i] - min_a >= b[i] - min_b:
            count += a[i] - min_a
        else:
            count += b[i] - min_b
    return count
        
t = int(input())
for num in range(t):
    n = int(input())
    a = list(map(int,input().strip().split()))[:n]
    b = list(map(int,input().strip().split()))[:n]
    result = findSteps(a,b)
    print(result)
