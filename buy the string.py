def find_min_coins(arr, s):
    n = arr[0]
    c0 = arr[1]
    c1 = arr[2]
    h = arr[3]
    no_0 = 0
    no_1 = 0
    for i in s:
        if i == '0':
            no_0 += 1
        else:
            no_1 += 1
    if c0 > (h + c1):
        return (no_1*c1) + (no_0*(h+c1))
    elif c1 > (h + c0):
        return (no_0*c0) + (no_1*(h+c0))
    else:
        return (no_0*c0) + (no_1*c1)

t = int(input())
for i in range(t):
    arr = list(map(int,input().strip().split()))[:4]
    s = input()
    result = find_min_coins(arr, s)
    print(result)
