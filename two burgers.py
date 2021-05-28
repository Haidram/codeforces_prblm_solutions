def find_cost(arr1,arr2):
    b = arr1[0]
    p = arr1[1]
    f = arr1[2]
    h = arr2[0]
    c = arr2[1]
    ham_flag = 0
    chick_flag = 0
    if h>=c:
        ham_flag = 1
    else:
        chick_flag = 1
    rem_b = 0
    num_h = 0
    num_c = 0
    if ham_flag == 1:
        if b >= 2*p:
            rem_b = b - 2*p
            num_h = p
        else:
            num_h = b//2
        if rem_b != 0:
            if rem_b >= 2*f:
                num_c = f
            else:
                num_c = rem_b//2
    else:
        if b >= 2*f:
            rem_b = b - 2*f
            num_c = f
        else:
            num_c = b//2
        if rem_b != 0:
            if rem_b >= 2*p:
                num_h = p
            else:
                num_h = rem_b//2
    return (num_h*h) + (num_c*c)

t = int(input())
for i in range(t):
    arr1 = list(map(int,input().strip().split()))[:3]
    arr2 = list(map(int,input().strip().split()))[:2]
    result = find_cost(arr1,arr2)
    print(result)
