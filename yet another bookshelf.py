def find_num(arr):
    start_index = arr.index(1)
    a = list(reversed(arr))
    end_index = a.index(1)
    end_index = len(arr) - end_index - 1
    count = 0
    for i in range(start_index+1,end_index):
        if arr[i] == 0:
            count += 1
    return count

t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int,input().strip().split()))[:n]
    result = find_num(arr)
    print(result)
