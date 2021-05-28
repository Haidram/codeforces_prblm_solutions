def findarr(x):
    arr = []
    for i in range(len(x)):
        if str(x[i]) not in arr:
            arr.append(str(x[i]))
    return arr

t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int,input().strip().split()))[:2*n]
    result = findarr(a)
    print(" ".join(result))
