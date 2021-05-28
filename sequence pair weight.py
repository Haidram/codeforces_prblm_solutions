def solve(n,arr):
    dic = {}
    for i in range(n):
        if arr[i] not in dic:
            dic[arr[i]] = []
        dic[arr[i]].append(i)

    count = 0
    for value in dic.values():
        if len(value) > 1:
            temp2 = 0
            for i in value:
                temp2 += n-i
            for i in value:
                temp2 -= n-i
                temp1 = i+1
                count += temp1*temp2
    return count

t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int,input().strip().split()))[:n]
    result = solve(n,arr)
    print(result)
