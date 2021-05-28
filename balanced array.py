def getArray(a):
    if a%4 == 1 or a%4 == 3 or a%4 == 2:
        print("NO")
    else:
        print("YES")
        arr = [0]*a
        j = k = 0
        while j < a//2:
            arr[j] = 2+k
            print(arr[j],end=" ")
            k += 4
            j += 1
        
        k = -1
        m = 0
        l = 0
        while j < a and l < a//2:
            arr[j] = arr[l] - k**m
            print(arr[j],end=" ")
            m += 1
            l += 1
        print()

t = int(input())
for i in range(t):
    n = int(input())
    getArray(n)
