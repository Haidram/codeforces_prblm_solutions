def findMin(n):
    count = 0
    for i in range(1,n//2):
        count += (2**i)
    for i in range(n//2,n-1):
        count -= (2**i)
    count += (2**n - 2**(n-1))
    return count

t = int(input())
for i in range(t):
    n = int(input())
    result = findMin(n)
    print(result)
