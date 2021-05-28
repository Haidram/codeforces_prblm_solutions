def solve(n, arr):
    s1 = "".join(str(arr))
    arr2 = sorted(arr)
    s2 = "".join(str(arr2))
    
    if s1 == s2:
        return '0'

    if int(arr[0]) == 1 or int(arr[n-1]) == n:
        return '1'

    if int(arr[0]) == n and int(arr[n-1]) == 1:
        return '3'

    return '2'
    
    
t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int,input().strip().split()))[:n]
    print(solve(n, arr))
    
    
