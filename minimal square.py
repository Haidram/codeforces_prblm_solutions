def find_sq(arr):
    l = arr[0]
    b = arr[1]
    if l > b:
        if 2*b >= l:
            side_length = 2*b
        else:
            side_length = l
    elif b > l:
        if 2*l >= b:
            side_length = 2*l
        else:
            side_length = b
    else:
        side_length = 2*l
    return side_length**2

t = int(input())
for i in range(t):
    a = list(map(int,input().strip().split()))[:2]
    sq_area = find_sq(a)
    print(sq_area)
