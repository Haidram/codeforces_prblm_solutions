def findSides(w,x,y,z):
    arrr = []
    k = y
    j = y
    i = x
    while i >= w:
        if i+j > k:
            arrr.extend([str(i), str(j), str(k)])
            return arrr
        i -= 1
                    
t = int(input())
for i in range(t):
    arr = list(map(int,input().strip().split()))[:4]
    a = arr[0]
    b = arr[1]
    c = arr[2]
    d = arr[3]
    result = findSides(a,b,c,d)
    print(" ".join(result))
