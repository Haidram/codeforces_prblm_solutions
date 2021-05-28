def find_area(a):
    arr = []
    for i in range(len(a)):
        for j in a[i+1:len(a)]:
            diff = j - a[i]
            if diff not in arr:
                arr.append(diff)
    return len(arr)

t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int,input().strip().split()))[:n]
    result = find_area(a)
    print(result)
