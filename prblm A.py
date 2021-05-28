def findans(a,arr):
    n = a[0]
    x = a[1]
    arr_final = []
    check_sum = 0
    arr.sort()
    num = -1
    for i in arr:
        if check_sum+i < x:
            arr_final.append(str(i))
            check_sum += i
        elif check_sum+i == x:
            num = arr.index(i)
        else:
            arr_final.append(str(i))
            check_sum += i
    if num != -1:
        arr_final.append(str(arr[num]))
        check_sum += arr[num]
    if check_sum == x:
        return 'NO',arr_final
    else:
        return 'YES',arr_final

t = int(input())
for i in range(t):
    a = list(map(int,input().strip().split()))[:2]
    arr = list(map(int,input().strip().split()))[:a[0]]
    result,arr1 = findans(a,arr)
    print(result)
    if result == 'YES':
        print(" ".join(arr1))
