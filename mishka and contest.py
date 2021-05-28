def findAns(arr, a):
    k = arr[1]
    n = arr[0]
    flag = False
    for i in a:
        if i > k:
            index_1 = a.index(i)
            flag = True
            break
    j = n
    while j >= 0:
        j -= 1
        if a[j] > k:
            index_2 = j
            break
    if flag:
        return ((n-1)-(index_2 - index_1))
    else:
        return n

arr = list(map(int,input().strip().split()))[:2]
a = list(map(int,input().strip().split()))[:arr[0]]
result = findAns(arr,a)
print(result)
