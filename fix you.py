t = int(input())
for i in range(t):
    arr = list(map(int,input().strip().split()))[:2]
    n = arr[0]
    m = arr[1]
    count = 0
    for j in range(n):
        s = input()
        if s[m-1] is 'R' and j != n-1:
            count += 1
        elif j == n-1:
            for k in s:
                if k is 'D':
                    count += 1
    print(count)
