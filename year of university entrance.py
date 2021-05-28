def solve(n, arr):
    if n == 1:
        return arr[0]

    arr = sorted(list(set(arr)))
    return arr[n//2]
    

n = int(input())
arr = list(map(int,input().strip().split()))[:n]
print(solve(n, arr))
    
