def solve(n,arr):
    count = 0
    b = [0]*n
    for i in range(n):
        b[i] = arr[i] - i
    dict_arr = {}
    for i in range(n):
        if b[i] not in dict_arr:
            dict_arr[b[i]] = 0
        dict_arr[b[i]] += 1
    for key,value in dict_arr.items():
        if value > 1:
            count += (value*(value-1))//2
    
    return count

t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int,input().strip().split()))[:n]
    print(solve(n,arr))
