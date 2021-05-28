def solve(arr):
    x = arr[0]
    n = arr[1]
    m = arr[2]
    
    while x > 19 and n > 0:
        x = x//2 + 10
        n -= 1
        
    while m > 0:
        x = x - 10
        m -= 1
        
    if x > 0:
        return 'NO'
    else:
        return 'YES'
        
t = int(input())
for i in range(t):
    arr = list(map(int,input().strip().split()))[:3]
    print(solve(arr))
