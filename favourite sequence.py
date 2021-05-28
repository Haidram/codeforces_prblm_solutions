def findArr(a,n):
    arr = [0]*(n)
    i = j = 0
    while i < n:
        arr[i] = str(a[j])
        i += 2
        j += 1
    j = n-1
    i = 1
    while i < n:
        arr[i] = str(a[j])
        i += 2
        j -= 1
    return " ".join(arr)
    
t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int,input().strip().split()))[:n]
    result = findArr(a,n)
    print(result)
