def find_max_len(arr):
    max_flag = 0               ##Result to return at last
    flag = 0                   ##To track the number of increasing nature
    for i in range(len(arr)-1):    ##Going throu the arr
        if arr[i] < arr[i+1]:     ##Checking if increasing
            flag += 1
        else:
            flag = 0
        if max_flag < flag:       ##max increasing arr length
            max_flag = flag
    return max_flag + 1

n = int(input())   ##Taking the input
arr = list(map(int,input().strip().split()))[:n]   ##Taking the array
result = find_max_len(arr)      ##Getting the result
print(result)
