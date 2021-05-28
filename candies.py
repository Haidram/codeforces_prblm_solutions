def solve(n, m):
    if n%m == 0:
        num = n//m
        arr = []
        for i in range(m):
            arr.append(str(num))
        return " ".join(arr)
    else:
        num = n//m
        rem = n - (num*m)
        i = 0
        arr = []
        while i < m:
            if i < m-rem:
                arr.append(str(num))
            else:
                arr.append(str(num+1))
            i += 1
        return " ".join(arr)
        

a = list(map(int,input().strip().split()))[:2]
n, m = a[0], a[1]
print(solve(n, m))
