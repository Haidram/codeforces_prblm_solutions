def solve(arr):
    a = arr[0]
    b = arr[1]

    n1 = 2*b + 1
    n2 = 2*b - 1
    n3 = 4*b

    num1 = n1*a
    num2 = n2*a
    num3 = n3*a
    str_num = ""
    str_num = str_num + str(num1) + " " + str(num2) + " " + str(num3)
    return str_num
    
t = int(input())
for i in range(t):
    arr = list(map(int,input().strip().split()))[:2]
    result = solve(arr)
    if arr[1] == 1:
        print("NO")
    else:
        print("YES")
        print(result)
