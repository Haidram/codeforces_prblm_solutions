def func(a,arr):
    n = a[0]
    l = a[1]
    r = a[2]
    count = 0
    
    # For storing color c[i] at ith position defining array for both left and right
    l_arr = [0]*(n+1)
    r_arr = [0]*(n+1)

    # For feeding color in left and right array
    for i in range(n):
        if i<l:
            l_arr[arr[i]] += 1
        else:
            r_arr[arr[i]] += 1

    # Cancelling all the socks which don't require any cost to get matching pair
    for i in range(n+1):
        min_num = min(l_arr[i], r_arr[i])
        l_arr[i] -= min_num
        r_arr[i] -= min_num

    # Now counting number of right and left socks in the array
    l_pair = r_pair = 0
    for i in range(n+1):
        if l_arr[i] > 0:
            l_pair += l_arr[i]
        if r_arr[i] > 0:
            r_pair += r_arr[i]
    
    # Counting socks of more than 1 color
    if l_pair > r_pair:
        count = abs(l_pair - r_pair) + r_pair
        transfer = (l_pair - r_pair)//2
        for i in range(n+1):
            while l_arr[i] > 1 and transfer > 0:
                l_arr[i] -= 2
                transfer -= 1
                count -= 1
    elif r_pair > l_pair:
        count = abs(l_pair - r_pair) + l_pair
        transfer = (r_pair - l_pair)//2
        for i in range(n+1):
            while r_arr[i] > 1 and transfer > 0:
                r_arr[i] -= 2
                transfer -= 1
                count -= 1
    else:
        count = l_pair

    return count

t = int(input())
for i in range(t):
    a = list(map(int,input().strip().split()))[:3]
    arr = list(map(int,input().strip().split()))[:a[0]]
    print(func(a,arr))
