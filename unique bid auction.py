def findWinner(a):
    b = []
    int_dict = {}
    for i in a:
        if i not in int_dict:
            int_dict[i] = 0
        int_dict[i] += 1
    for i in int_dict:
        if int_dict[i] == 1:
            b.append(i)
    b.sort()
    if len(b) == 0:
        return -1
    else:
        return (a.index(b[0]) + 1)

t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int,input().strip().split()))[:n]
    result = findWinner(arr)
    print(result)
