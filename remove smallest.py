def get_val(arr):
    num = len(arr)
    if num == 1:
        return "YES"
    for j in range(num):
        for k in range(num-j-1):
            if arr[k] > arr[k+1]:
                temp = arr[k]
                arr[k] = arr[k+1]
                arr[k+1] = temp
    for j in range(num-1):
        if arr[j+1]-arr[j] >1:
            return "NO"
    return "YES"
            
t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int,input().strip().split()))[:n]
    strarr = get_val(a)
    print(strarr)
