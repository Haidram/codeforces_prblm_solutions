def find_min_diff(a, arr):
    n = a[0]
    k = a[1]
    arr.sort()
    if k == 0:
        return arr[n-1] - arr[0]
    i = 1
    while i <= k:
        arr[n-1] += arr[n-1-i]
        i += 1
    return arr[n-1]

t = int(input())
for i in range(t):
    a = list(map(int,input().strip().split()))[:2]
    arr = list(map(int,input().strip().split()))[:a[0]]
    result = find_min_diff(a, arr)
    print("The result is: ",result) 
