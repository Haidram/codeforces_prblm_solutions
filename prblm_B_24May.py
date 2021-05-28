def solve(n, a):
    count = 0
    arr = []
    b = []
    for i in a:
        if i <= 0:
            count += 1
            arr.append(i)
        else:
            b.append(i)

    min_diff = 10**9
    arr = sorted(arr)
    i = 0
    while i < count - 1:
        if abs(arr[i]-arr[i+1]) < min_diff:
            min_diff = abs(arr[i]-arr[i+1])
        i += 1
    for j in b:
        if j <= min_diff:
            count += 1
            break

    return count


t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int,input().strip().split()))[:n]
    print(solve(n, a))
